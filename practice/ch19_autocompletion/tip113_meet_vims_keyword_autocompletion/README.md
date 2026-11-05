# Tip 113: Meet Vim's Keyword Autocompletion with <C-n> and <C-p>

> **출처**: 《Practical Vim, Second Edition》 p. 279  
> **챕터**: Dial X for Autocompletion (ch19_autocompletion)

---

## 🎯 Concept (학습 목표)
Insert Mode (삽입 모드)에서 <C-n>(다음 일치) 및 <C-p>(이전 일치) 단축키로 현재 버퍼 및 로드된 버퍼의 단어를 기반으로 Keyword Completion (키워드 자동완성)을 실행합니다.

---

## 📝 Mission (실습 미션)
She sells sea 뒤에서 <C-p>를 입력하여 버퍼에 존재하는 shells를 자동완성하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`G` `A` `sh` `<C-p>` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 113
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 113
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 113
   ```
