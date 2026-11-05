# Tip 14: Get Back to Normal Mode with <C-o>

> **출처**: 《Practical Vim, Second Edition》 p. 29  
> **챕터**: Insert Mode (ch03_insert_mode)

---

## 🎯 Concept (학습 목표)
<C-o>는 삽입 모드에서 단 한 번의 노멀 모드 명령어를 실행하고 다시 삽입 모드를 유지합니다.

---

## 📝 Mission (실습 미션)
입력 중 <C-o>zz 를 눌러 화면 중앙 정렬 후 입력을 이어가세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`A` ` text` `<C-o>zz` ` continue` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 14
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 14
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 14
   ```
