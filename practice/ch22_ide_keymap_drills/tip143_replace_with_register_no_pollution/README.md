# Tip 143: Drill 09: Replace with Register without Clipboard Pollution

> **출처**: 《Practical Vim, Second Edition》 Keymap Drill #9  
> **챕터**: Cross-IDE Situational Keymap Drills (ch22_ide_keymap_drills)

---

## 🎯 Concept (학습 목표)
Yank Inner Word (yiw: 원본 단어 복사) 후 Replace With Register (griw: 레지스터 대체)를 사용하면 클립보드 오염 없이 연속 텍스트 치환이 가능합니다.

---

## 📝 Mission (실습 미션)
첫 단어 ACTIVE 를 복사하여 PENDING 과 INACTIVE 를 모두 ACTIVE 로 덮어쓰세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`0yiwwgriwwgriw`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 143
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 143
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 143
   ```
