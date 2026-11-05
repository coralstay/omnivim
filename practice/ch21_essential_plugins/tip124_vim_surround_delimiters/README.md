# Tip 124: Add, Change, or Delete Delimiters (vim-surround)

> **출처**: 《Practical Vim, Second Edition》 Plugin Track #1  
> **챕터**: Essential Modern Plugins (ch21_essential_plugins)

---

## 🎯 Concept (학습 목표)
cs"' 로 큰따옴표를 작은따옴표로, ds" 로 따옴표를 삭제하고, ysiw] 로 대괄호를 씌웁니다.

---

## 📝 Mission (실습 미션)
cs"' 후 ds" 및 ysiw] 를 수행하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`cs"'` `j` `ds"` `j` `ysiw]`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 124
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 124
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 124
   ```
