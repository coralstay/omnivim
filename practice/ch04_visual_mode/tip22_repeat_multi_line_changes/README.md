# Tip 22: Repeat Multi-Line Changes

> **출처**: 《Practical Vim, Second Edition》 p. 45  
> **챕터**: Visual Mode (ch04_visual_mode)

---

## 🎯 Concept (학습 목표)
V로 여러 줄을 선택 후 > 로 들여쓰기하고, . 로 반복합니다.

---

## 📝 Mission (실습 미션)
jVj > 로 들여쓰기하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`j` `V` `j` `>` `>`**

---

## 📂 실습 파일 안내
- **`practice.py`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.py`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 22
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.py`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 22
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 22
   ```
