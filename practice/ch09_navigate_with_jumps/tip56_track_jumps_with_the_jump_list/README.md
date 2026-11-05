# Tip 56: Track Jumps with Jump List (<C-o>, <C-i>)

> **출처**: 《Practical Vim, Second Edition》 p. 130  
> **챕터**: Navigate with Jumps (ch09_navigate_with_jumps)

---

## 🎯 Concept (학습 목표)
<C-o>로 이전 점프 위치(웹 브라우저의 뒤로 가기)로, <C-i>로 앞으로 갑니다.

---

## 📝 Mission (실습 미션)
G 점프 후 <C-o> 로 복귀하여 x 로 J를 삭제하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`G` `<C-o>` `x`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 56
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 56
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 56
   ```
