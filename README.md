# RCY Network — Apple-inspired HTML concept

RCY Network를 Apple이 설계한다는 가정 아래 만든 정적 프런트엔드 콘셉트입니다. Apple의 화면이나 자산을 복제하지 않고, 대형 타이포그래피·넓은 여백·제품 중심 스토리텔링·절제된 모션을 RCY Network에 맞게 재해석했습니다.

## Pages

- `index.html` — 전국 RCY Network 랜딩페이지
- `dashboard.html` — 회원 대시보드
- `school.html` — 학교 공개 랜딩페이지(대구가톨릭대학교 RCY 예시)
- `styles.css` — 공통 디자인 시스템과 반응형 스타일
- `script.js` — 메뉴, 스크롤 노출, 카운터, 토스트 인터랙션

## Run locally

```bash
python3 -m http.server 8080
```

브라우저에서 `http://localhost:8080`을 엽니다. 별도 빌드 과정이나 패키지는 필요하지 않습니다.

## Design principles

- 시스템 폰트만 사용한 빠른 로딩과 네이티브한 인상
- 흑백 중심 화면에 RCY 적색을 핵심 행동과 검증 상태에만 사용
- 전국 플랫폼, 개인, 학교의 세 맥락을 하나의 디자인 토큰으로 통합
- 모바일 메뉴, 대시보드 하단 내비게이션, 키보드 포커스, reduced-motion 지원
- 외부 이미지와 UI 라이브러리 없이 실행 가능한 독립형 HTML

> 수치와 인물 정보 일부는 화면 구성을 위한 예시 데이터입니다.
