# Tip 45: Keep Your Fingers on the Home Row

> **출처**: 《Practical Vim, Second Edition》 p. 105  
> **챕터**: Motions & Text Objects (ch08_navigate_with_motions)

---

## 🎯 Concept (학습 목표)
h, j, k, l 기본 이동키를 손에 완전히 익힙니다.

---

## 📝 Mission (실습 미션)
j 로 아래 줄로 이동한 뒤 x 로 X 글자를 삭제하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`j` `x`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 45
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 45
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 45
   ```
