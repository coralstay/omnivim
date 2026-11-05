# Tip 131: Swap Words with vim-exchange

> **출처**: 《Practical Vim, Second Edition》 Plugin Track #8  
> **챕터**: Essential Modern Plugins (ch21_essential_plugins)

---

## 🎯 Concept (학습 목표)
cxiw 로 첫 단어를 마킹하고 다른 단어에서 cxiw 를 누르면 두 단어의 위치가 맞교환됩니다.

---

## 📝 Mission (실습 미션)
cxiw 로 두 단어 위치를 맞바꾸세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`cxiw` `w` `cxiw`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 131
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 131
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 131
   ```
