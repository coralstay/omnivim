# Tip 118: Autocomplete Filenames with <C-x><C-f>

> **출처**: 《Practical Vim, Second Edition》 p. 293  
> **챕터**: Dial X for Autocompletion (ch19_autocompletion)

---

## 🎯 Concept (학습 목표)
<C-x><C-f> 단축키는 로컬 파일시스템의 경로를 탐색하여 Filename Completion (파일명 자동완성)을 수행합니다.

---

## 📝 Mission (실습 미션)
경로 뒤에 파일명 mcp_server.py를 완성하여 올바른 모듈 임포트를 완성하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`GA` `mcp_server.py");` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.js`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.js`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 118
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.js`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 118
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 118
   ```
