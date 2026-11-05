# Tip 62: Replace Visual Selection with Register

> **출처**: 《Practical Vim, Second Edition》 p. 147  
> **챕터**: Copy and Paste (ch10_copy_and_paste)

---

## 🎯 Concept (학습 목표)
Visual 모드에서 p를 누르면 선택 영역을 레지스터 내용으로 교체합니다 (또는 griw 활용).

---

## 📝 Mission (실습 미션)
단어 복사 후 다른 단어를 Visual 선택하여 p 로 덮어쓰세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`yiw` `w` `ve` `p`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 62
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 62
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 62
   ```
