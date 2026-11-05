# Tip 12: Combine Operators with Motions

> **출처**: 《Practical Vim, Second Edition》 p. 23  
> **챕터**: Normal Mode (ch02_normal_mode)

---

## 🎯 Concept (학습 목표)
Operator + Motion = Action 공식을 익힙니다: d, c, y, gU, gu 와 w, b, $, iw 조합.

---

## 📝 Mission (실습 미션)
wgUiw로 현재 단어를 대문자로 바꾸고, j0ci"로 따옴표 안을 수정하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`w` `gUiw` `j` `0` `ci"` `updated` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 12
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 12
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 12
   ```
