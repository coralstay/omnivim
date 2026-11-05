# Tip 13: Make Corrections Instantly from Insert Mode

> **출처**: 《Practical Vim, Second Edition》 p. 27  
> **챕터**: Insert Mode (ch03_insert_mode)

---

## 🎯 Concept (학습 목표)
<C-h>(백스페이스), <C-w>(앞 단어 삭제), <C-u>(줄 시작까지 삭제)로 입력 모드 탈출 없이 수정합니다.

---

## 📝 Mission (실습 미션)
오타 입력 중 <C-w>를 눌러 직전 단어를 지우고 올바르게 입력하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`A` ` wrongword` `<C-w>` `correct` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 13
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 13
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 13
   ```
