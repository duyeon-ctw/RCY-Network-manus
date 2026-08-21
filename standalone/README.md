# RCY Network — Standalone HTML

이 폴더의 HTML은 각 파일 안에 CSS, JavaScript, SVG 아이콘이 모두 포함된 단일 파일 버전입니다. 별도의 `styles.css`, `script.js`, npm 설치 또는 빌드 과정 없이 파일을 브라우저에서 바로 열 수 있습니다.

## Pages

- `activities.html`
- `activity.html`
- `dashboard.html`
- `hours.html`
- `index.html`
- `join.html`
- `messages.html`
- `organization.html`
- `profile.html`
- `school.html`
- `schools.html`
- `settings.html`

페이지 자체의 디자인과 인터랙션은 파일 하나만으로 작동합니다. 다른 화면으로 이동하는 내부 링크까지 사용하려면 관련 HTML을 같은 폴더에 함께 두세요.

이 폴더는 `python tools/build_standalone.py` 또는 GitHub Actions로 `apple-v2/` 소스에서 자동 생성됩니다.
