# Tip 26: Append After a Ragged Right Visual Block

> **출처**: 《Practical Vim, Second Edition》 p. 52  
> **챕터**: Visual Mode (ch04_visual_mode)

---

## 🎯 Concept (학습 목표)
길이가 다른 여러 줄도 <C-v> {j...} $ A ; <Esc> 로 각 줄 끝에 동시에 텍스트를 추가할 수 있습니다.

---

## 📝 Mission (실습 미션)
<C-v>2j $ A ; <Esc> 로 세 줄 끝에 세미콜론을 일괄 추가하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`<C-v>` `2j` `$` `A` `;` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.css`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.css`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 26
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.css`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 26
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 26
   ```
