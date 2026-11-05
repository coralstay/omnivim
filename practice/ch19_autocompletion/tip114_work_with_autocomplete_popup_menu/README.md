# Tip 114: Work with the Autocomplete Pop-Up Menu

> **출처**: 《Practical Vim, Second Edition》 p. 282  
> **챕터**: Dial X for Autocompletion (ch19_autocompletion)

---

## 🎯 Concept (학습 목표)
Vim의 Pop-Up Menu (팝업 메뉴)에서 <C-n>과 <C-p>로 후보군을 순회하고, 원하는 항목이 선택되었을 때 타이핑을 계속하거나 <C-y>(Yes)로 수락합니다.

---

## 📝 Mission (실습 미션)
au 뒤에서 <C-n>을 눌러 목록 중 automate를 선택하여 문장을 완성하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`G` `A` `<C-n>` `<C-n>` `<C-n>` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 114
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 114
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 114
   ```
