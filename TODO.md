# 모바일 청첩장 TODO

> 김용환 ♥ 최한솔 · 2026.09.12 (토) · 강남 브라이튼 하우스
> 배포: https://socialbiz1.github.io/wedding/

---

## ✅ 완료 (2026-04-30)

- [x] 소개 페이지 → 모바일 청첩장으로 전면 재구성
- [x] 11개 섹션 골격 완성 (Hero / 인사말 / 신랑신부 / 갤러리 / 예식안내 / 오시는길 / D-Day / 마음전하실곳 / RSVP / 방명록 / 공유)
- [x] 9월 캘린더 그리드 (12일 강조)
- [x] 계좌번호 클립보드 복사 + 토스트
- [x] RSVP·방명록 localStorage 임시 구현
- [x] 라이트박스, D-Day 카운트다운 유지
- [x] 갤러리 12장 그리드 + 더보기 토글
- [x] 모바일 폭(480px) 컨테이너 + OG 메타

---

## 🔜 남은 작업

### 1) 폰트 교체
- 현재: `Noto Sans KR` + `Nanum Myeongjo`
- 교체 후보 검토 (예: Pretendard / GowunDodum / Gaegu / IBM Plex Sans KR / 명조 계열 변경 등)
- 결정 시 `<link>` 와 `:root --serif / --sans` 두 곳만 바꾸면 됨

### 2) 상세 내용 채우기 (◯◯◯ 자리)
- [ ] 양가 부모님 성함 — `.person-parents` 4곳
- [ ] 예식 시각 — `.event-time` + `.hero-when` 보강 시 시각 추가
- [ ] 정확한 홀 이름 — `.event-hall`
- [ ] 정확한 주소 — `.address-detail`
- [ ] 지하철/버스/주차 — `.transport-text` 3개
- [ ] 신랑 전화번호 — `tel:` `sms:` 2곳 + `copyAccount` 데이터
- [ ] 신부 전화번호 — `tel:` `sms:` 2곳
- [ ] 혼주 4명 전화번호 — `.contact-group .contact-row`
- [ ] 계좌번호 6개 — `.gift-row` × 6 (은행명 + 계좌번호 + `copyAccount` 인자)
- [ ] 인사말 톤 조정 — `.greeting-text` (현재는 표준 문구)
- [ ] 지도 앱 링크 — 네이버/카카오/티맵 검색어 또는 정확한 좌표로 교체

### 3) 사진 추가
모두 `wedding_intro/photos/` 폴더에 넣으면 자동 인식 (없으면 placeholder 표시)

- [ ] `couple.jpg` — 히어로 대표 사진 (세로 비율 권장, 약 3:4)
- [ ] `gallery_1.jpg` ~ `gallery_12.jpg` — 갤러리 (3:4 비율, 12장)
- [ ] `map.jpg` — 오시는 길 약도 이미지 (4:3 비율)

### 4) 외부 서비스 연동 (선택)
- [ ] **카카오톡 공유** — Kakao SDK 앱키 발급 → `shareKakao()` 함수 교체
  - 참고: https://developers.kakao.com/docs/latest/ko/message/js-link
- [ ] **RSVP 영구 저장** — 현재 localStorage(브라우저별 분리). 옵션:
  - 가장 쉬움: 구글폼 임베드 또는 링크 버튼으로 교체
  - 통합 관리: Firebase Firestore 또는 Supabase
- [ ] **방명록 영구 저장** — RSVP와 동일 옵션

---

## 📁 파일 위치

- 로컬: `C:\Users\NHN\wedding_intro\index.html`
- 배포: GitHub Pages (`socialbiz1.github.io/wedding/`)
- 사진: `C:\Users\NHN\wedding_intro\photos\` (생성 필요)

## 📌 디자인 토큰 (수정 시 참고)

```css
--cream: #fdf8f3   /* 메인 배경 */
--blush: #f2e0d5   /* 강조 배경 */
--rose:  #c9876b   /* 메인 포인트 */
--deep:  #7a4f3a   /* 진한 텍스트 */
--gold:  #c8a97e   /* 라벨/포인트 */
```
