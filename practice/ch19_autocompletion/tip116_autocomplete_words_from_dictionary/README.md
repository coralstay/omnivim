# Tip 116: Autocomplete Words from the Dictionary with <C-x><C-k>

> **출처**: 《Practical Vim, Second Edition》 p. 288  
> **챕터**: Dial X for Autocompletion (ch19_autocompletion)

---

## 🎯 Concept (학습 목표)
<C-x><C-k> 단축키는 현재 문서에 없는 단어라도 시스템 사전에 등재된 올바른 어휘를 검색하여 Dictionary Completion (사전 자동완성)을 수행합니다.

---

## 📝 Mission (실습 미션)
indiscrimin 뒤에서 ate를 입력하여 discriminate 철자를 완성하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`GA` `ate` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 116
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 116
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 116
   ```
