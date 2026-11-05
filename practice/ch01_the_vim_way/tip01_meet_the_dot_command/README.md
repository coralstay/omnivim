# Tip 1: Meet the Dot Command

> **출처**: 《Practical Vim, Second Edition》 p. 2  
> **챕터**: The Vim Way (ch01_the_vim_way)

---

## 🎯 Concept (학습 목표)
마침표(.) 명령어는 직전의 Change (변경 작업)을 그대로 재실행합니다.

---

## 📝 Mission (실습 미션)
각 줄 끝에 세미콜론(;)을 추가하세요. 첫 행에서 A; 후 j. j. 로 완료하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`A` `;` `<Esc>` `j` `.` `j` `.`**

---

## 📂 실습 파일 안내
- **`practice.js`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.js`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 1
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.js`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 1
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 1
   ```
