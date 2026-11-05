# Tip 6: Meet the Dot Formula

> **출처**: 《Practical Vim, Second Edition》 p. 13  
> **챕터**: The Vim Way (ch01_the_vim_way)

---

## 🎯 Concept (학습 목표)
이상적인 One-stroke (원 스트로크) 이동과 One-stroke 변경의 조합으로 극상의 타이핑 효율을 달성합니다.

---

## 📝 Mission (실습 미션)
각 줄의 공백을 f+ s + <Esc> 후 ; . 로 정돈하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`f+` `s` ` + ` `<Esc>` `;` `.`**

---

## 📂 실습 파일 안내
- **`practice.js`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.js`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 6
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.js`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 6
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 6
   ```
