# Tip 112: Grep with Vim's Internal Search Engine with :vimgrep

> **출처**: 《Practical Vim, Second Edition》 p. 276  
> **챕터**: Search Project-Wide with Grep (ch18_grep)

---

## 🎯 Concept (학습 목표)
:vimgrep /pattern/ **/* 로 외부 도구 없이 Vim 고유의 정규식 엔진으로 전체 검색합니다.

---

## 📝 Mission (실습 미션)
:%s/needle/found/g<CR> 로 needle 을 found 로 변경하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`:%s/needle/found/g<CR>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 112
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 112
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 112
   ```
