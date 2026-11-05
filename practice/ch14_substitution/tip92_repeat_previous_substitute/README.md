# Tip 92: Repeat Previous Substitute with :&

> **출처**: 《Practical Vim, Second Edition》 p. 221  
> **챕터**: Substitution (ch14_substitution)

---

## 🎯 Concept (학습 목표)
:& 또는 :&& 로 이전 치환 명령을 현재 줄 또는 다른 범위에 동일한 플래그로 재실행합니다.

---

## 📝 Mission (실습 미션)
:s/cat/dog/<CR> 후 j 이동하여 :&<CR> 로 반복하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`:s/cat/dog/<CR>` `j` `:&<CR>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 92
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 92
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 92
   ```
