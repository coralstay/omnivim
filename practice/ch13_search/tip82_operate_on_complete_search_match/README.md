# Tip 82: Operate on Complete Search Match with gn

> **출처**: 《Practical Vim, Second Edition》 p. 199  
> **챕터**: Search (ch13_search)

---

## 🎯 Concept (학습 목표)
gn 텍스트 오브젝트는 다음 검색 매치 전체를 선택하거나 dgn, cgn 등 오퍼레이터를 적용합니다.

---

## 📝 Mission (실습 미션)
cgn 으로 다음 일치 단어를 즉시 교체하고 . 로 반복하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`/target<CR>` `cgn` `new` `<Esc>` `.`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 82
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 82
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 82
   ```
