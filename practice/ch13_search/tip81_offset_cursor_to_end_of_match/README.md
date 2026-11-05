# Tip 81: Offset Cursor to the End of Match with /e

> **출처**: 《Practical Vim, Second Edition》 p. 197  
> **챕터**: Search (ch13_search)

---

## 🎯 Concept (학습 목표)
/pattern/e 로 검색하면 커서가 매칭된 단어의 시작이 아닌 끝으로 바로 이동합니다.

---

## 📝 Mission (실습 미션)
/tag/e<CR> 로 단어 끝으로 이동한 뒤 a_end<Esc> 를 추가하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`/tag/e<CR>` `a_end<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 81
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 81
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 81
   ```
