# Tip 130: Replace with Register without Overwriting Clipboard

> **출처**: 《Practical Vim, Second Edition》 Plugin Track #7  
> **챕터**: Essential Modern Plugins (ch21_essential_plugins)

---

## 🎯 Concept (학습 목표)
griw 로 레지스터를 오염시키지 않고 대상을 복사된 내용으로 덮어씁니다.

---

## 📝 Mission (실습 미션)
yiw 후 griw 로 대상을 교체하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`yiw` `w` `griw`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 130
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 130
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 130
   ```
