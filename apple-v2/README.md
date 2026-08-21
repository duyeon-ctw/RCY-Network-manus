# RCY Network — Apple-inspired HTML Concept v2

RCY Network를 Apple이 설계한다는 가정으로 만든 정적 HTML 프런트엔드 콘셉트입니다. Apple의 화면, 문구, 이미지나 상표 자산을 복제하지 않고 다음 원칙을 RCY Network의 서비스 구조에 맞게 재해석했습니다.

- 44px 글로벌 내비게이션과 페이지별 로컬 내비게이션
- 한 섹션에 하나의 핵심 메시지를 전달하는 대형 타이포그래피
- 제품 렌더처럼 보이는 CSS 기반 UI 시각화
- 넓은 여백, 1px 구분선, 절제된 그림자와 반투명 소재
- 스크롤 스토리텔링, 카운터, 필터, 아코디언, 모달, 토스트
- 모바일 앱 하단 내비게이션과 반응형 상세 화면
- 외부 이미지·UI 라이브러리·빌드 도구가 필요 없는 독립형 HTML

## Pages

### Public

- `index.html` — RCY Network 제품형 랜딩페이지
- `schools.html` — 전국 학교 및 조직 탐색
- `school.html` — 대구가톨릭대학교 RCY 공개 페이지
- `join.html` — 4단계 회원 가입 신청
- `activity.html` — 활동 상세 및 신청

### Member app

- `dashboard.html` — 개인 홈 및 임팩트 대시보드
- `activities.html` — 활동 검색, 필터와 추천
- `hours.html` — 검증 봉사시간과 증빙 원장
- `profile.html` — 공개 프로필, 배지와 활동 타임라인
- `messages.html` — 조직 및 개인 메시지
- `settings.html` — 계정, 보안, 공개범위와 알림

### Organization

- `organization.html` — 학교 운영 콘솔, 모집 퍼널, 승인, 회원 관리

## Run locally

```bash
python3 -m http.server 8080
```

브라우저에서 `http://localhost:8080/apple-v2/`를 엽니다. 별도 빌드 과정이나 패키지는 필요하지 않습니다.

## Notes

- 수치, 인물, 활동, 학교 정보 일부는 디자인 시연용 예시입니다.
- 실제 서비스에서는 서버 인증, 권한 검사, 개인정보 최소수집, 데이터 검증, 접근성 테스트와 백엔드 연동이 추가로 필요합니다.
