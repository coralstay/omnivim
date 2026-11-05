# Tip 2: Don't Repeat Yourself (DRY)

> **출처**: 《Practical Vim, Second Edition》 p. 4  
> **챕터**: The Vim Way (ch01_the_vim_way)

---

## 🎯 Concept (학습 목표)
$a; 대신 A; 를 사용하면 이동과 삽입을 하나의 원자적 변경으로 묶어 . 명령어로 재사용할 수 있습니다.

---

## 📝 Mission (실습 미션)
$a; 대신 A; 를 사용하여 마침표 공식의 이점을 체득하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`A` `;` `<Esc>` `j` `.` `j` `.`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 2
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 2
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 2
   ```
