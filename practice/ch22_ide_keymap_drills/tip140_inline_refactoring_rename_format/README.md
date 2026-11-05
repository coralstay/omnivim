# Tip 140: Drill 06: Three-Step Inline Refactoring (Rename, Intention, Format)

> **출처**: 《Practical Vim, Second Edition》 Keymap Drill #6  
> **챕터**: Cross-IDE Situational Keymap Drills (ch22_ide_keymap_drills)

---

## 🎯 Concept (학습 목표)
RenameElement (<Space>cr: 심볼 이름 일괄 변경), Intention Actions (<Space>ca: 빠른 수정 및 인텐션 액션), ReformatCode (<Space>cf: 코드 서식 자동 정렬)의 3단계를 수행합니다.

---

## 📝 Mission (실습 미션)
변수명 usrNm 을 userName 으로 수정하고, 들여쓰기를 표준 2스페이스로 정리하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`:%s/usrNm/userName/g<CR>` `2G0i  <Esc>`**

---

## 📂 실습 파일 안내
- **`practice.js`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.js`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 140
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.js`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 140
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 140
   ```
