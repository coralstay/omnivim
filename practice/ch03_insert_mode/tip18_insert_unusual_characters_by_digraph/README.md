# Tip 18: Insert Unusual Characters by Digraph

> **출처**: 《Practical Vim, Second Edition》 p. 35  
> **챕터**: Insert Mode (ch03_insert_mode)

---

## 🎯 Concept (학습 목표)
<C-k>{char1}{char2} 다이그래프 단축키로 특수문자를 직관적으로 입력합니다 (예: <C-k>Co -> ©, <C-k>12 -> ½).

---

## 📝 Mission (실습 미션)
<C-k>12 를 입력하여 ½ 분수 기호를 삽입하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`A` ` <C-k>12` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 18
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 18
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 18
   ```
