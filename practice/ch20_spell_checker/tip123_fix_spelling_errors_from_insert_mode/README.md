# Tip 123: Fix Spelling Errors from Insert Mode with <C-x>s

> **출처**: 《Practical Vim, Second Edition》 p. 308  
> **챕터**: Find and Fix Typos with Vim's Spell Checker (ch20_spell_checker)

---

## 🎯 Concept (학습 목표)
Insert Mode (삽입 모드)에서 탈출하지 않고도 <C-x>s를 누르면 직전 단어의 철자 교정 팝업이 호출되어 흐름을 깨지 않고 즉시 수정할 수 있습니다.

---

## 📝 Mission (실습 미션)
오타가 난 recieve를 올바른 철자 receive로 수정하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`0` `3w` `ciw` `receive` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 123
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 123
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 123
   ```
