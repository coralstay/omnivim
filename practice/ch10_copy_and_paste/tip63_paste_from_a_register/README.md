# Tip 63: Paste from a Register with "_ Black Hole

> **출처**: 《Practical Vim, Second Edition》 p. 149  
> **챕터**: Copy and Paste (ch10_copy_and_paste)

---

## 🎯 Concept (학습 목표)
"_dd 는 블랙홀 레지스터를 사용하여 레지스터를 전혀 오염시키지 않고 순수 삭제합니다.

---

## 📝 Mission (실습 미션)
"_dd 로 레지스터 손상 없이 행을 삭제하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`"_dd`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 63
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 63
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 63
   ```
