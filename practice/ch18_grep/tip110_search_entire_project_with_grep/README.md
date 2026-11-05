# Tip 110: Search the Entire Project with :grep

> **출처**: 《Practical Vim, Second Edition》 p. 271  
> **챕터**: Search Project-Wide with Grep (ch18_grep)

---

## 🎯 Concept (학습 목표)
:grep {pattern} * 로 프로젝트 전체 파일에서 검색하고 퀵픽스 목록으로 점프합니다.

---

## 📝 Mission (실습 미션)
:%s/TODO/DONE/g<CR> 로 TODO 를 DONE 으로 일괄 변경하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`:%s/TODO/DONE/g<CR>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 110
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 110
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 110
   ```
