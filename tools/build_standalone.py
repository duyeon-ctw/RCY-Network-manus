from __future__ import annotations

import re
import shutil
from pathlib import Path

SOURCE = Path("apple-v2")
OUTPUT = Path("standalone")


def load_css() -> str:
    manifest_path = SOURCE / "styles.css"
    manifest = manifest_path.read_text(encoding="utf-8")
    imports = re.findall(
        r"@import\s+url\([\"']?([^\"')]+)[\"']?\)\s*;",
        manifest,
        flags=re.IGNORECASE,
    )
    if not imports:
        raise RuntimeError("apple-v2/styles.css에서 @import 항목을 찾지 못했습니다.")

    parts: list[str] = []
    for relative_path in imports:
        css_path = SOURCE / relative_path
        if not css_path.is_file():
            raise FileNotFoundError(css_path)
        parts.append(
            f"/* ===== {relative_path} ===== */\n"
            f"{css_path.read_text(encoding='utf-8').rstrip()}"
        )
    return "\n\n".join(parts)


def build_page(source_path: Path, css: str, javascript: str) -> str:
    document = source_path.read_text(encoding="utf-8")

    style_block = (
        '<style id="rcy-network-inline-styles">\n'
        "/* RCY Network standalone build: all CSS is embedded in this file. */\n"
        f"{css}\n"
        "</style>"
    )
    script_block = (
        '<script id="rcy-network-inline-script">\n'
        "/* RCY Network standalone build: all JavaScript is embedded in this file. */\n"
        f"{javascript}\n"
        "</script>"
    )

    stylesheet_pattern = re.compile(
        r"<link\b(?=[^>]*\brel=[\"']stylesheet[\"'])"
        r"(?=[^>]*\bhref=[\"']styles\.css[\"'])[^>]*>",
        flags=re.IGNORECASE,
    )
    script_pattern = re.compile(
        r"<script\b(?=[^>]*\bsrc=[\"']script\.js[\"'])[^>]*>\s*</script>",
        flags=re.IGNORECASE,
    )

    document, stylesheet_count = stylesheet_pattern.subn(style_block, document, count=1)
    document, script_count = script_pattern.subn("", document, count=1)

    if stylesheet_count != 1:
        raise RuntimeError(
            f"{source_path}: styles.css 링크가 정확히 한 개가 아닙니다: {stylesheet_count}"
        )
    if script_count != 1:
        raise RuntimeError(
            f"{source_path}: script.js 태그가 정확히 한 개가 아닙니다: {script_count}"
        )
    if not re.search(r"</body>", document, flags=re.IGNORECASE):
        raise RuntimeError(f"{source_path}: </body>가 없습니다.")

    document = re.sub(
        r"</body>",
        f"{script_block}\n</body>",
        document,
        count=1,
        flags=re.IGNORECASE,
    )
    return document


def validate_page(path: Path) -> None:
    document = path.read_text(encoding="utf-8")
    checks = {
        "inline style": document.count('id="rcy-network-inline-styles"') == 1,
        "inline script": document.count('id="rcy-network-inline-script"') == 1,
        "no styles.css dependency": 'href="styles.css"' not in document,
        "no script.js dependency": 'src="script.js"' not in document,
        "no CSS import": "@import" not in document,
    }
    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        raise RuntimeError(f"{path}: 검증 실패 — {', '.join(failed)}")


def write_readme(page_names: list[str]) -> None:
    page_list = "\n".join(f"- `{name}`" for name in page_names)
    readme = f"""# RCY Network — Standalone HTML

이 폴더의 HTML은 각 파일 안에 CSS, JavaScript, SVG 아이콘이 모두 포함된 단일 파일 버전입니다. 별도의 `styles.css`, `script.js`, npm 설치 또는 빌드 과정 없이 파일을 브라우저에서 바로 열 수 있습니다.

## Pages

{page_list}

페이지 자체의 디자인과 인터랙션은 파일 하나만으로 작동합니다. 다른 화면으로 이동하는 내부 링크까지 사용하려면 관련 HTML을 같은 폴더에 함께 두세요.

이 폴더는 `python tools/build_standalone.py` 또는 GitHub Actions로 `apple-v2/` 소스에서 자동 생성됩니다.
"""
    (OUTPUT / "README.md").write_text(readme, encoding="utf-8")


def main() -> None:
    if not SOURCE.is_dir():
        raise FileNotFoundError(SOURCE)

    css = load_css()
    javascript = (SOURCE / "script.js").read_text(encoding="utf-8").rstrip()
    javascript = re.sub(r"</script", r"<\\/script", javascript, flags=re.IGNORECASE)

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    html_files = sorted(SOURCE.glob("*.html"))
    if not html_files:
        raise RuntimeError("apple-v2에 HTML 파일이 없습니다.")

    generated: list[str] = []
    for source_path in html_files:
        output_path = OUTPUT / source_path.name
        output_path.write_text(
            build_page(source_path, css, javascript),
            encoding="utf-8",
        )
        validate_page(output_path)
        generated.append(output_path.name)
        print(f"generated: {output_path} ({output_path.stat().st_size:,} bytes)")

    write_readme(generated)
    print(f"completed: {len(generated)} standalone HTML files")


if __name__ == "__main__":
    main()
