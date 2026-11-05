# Tip 138: Drill 04: Toggle Embedded Terminal and Context Return

> **출처**: 《Practical Vim, Second Edition》 Keymap Drill #4  
> **챕터**: Cross-IDE Situational Keymap Drills (ch22_ide_keymap_drills)

---

## 🎯 Concept (학습 목표)
ActivateTerminalToolWindow (<Space>t: 내장 터미널 토글)로 쉘 명령을 실행하고, FocusEditor (<Esc>: 에디터 복귀)로 편집 컨텍스트로 신속히 복귀합니다.

---

## 📝 Mission (실습 미션)
터미널 환경 점검 주석 끝에 // Terminal check completed 를 추가하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`Go// Terminal check completed<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.sh`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.sh`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 138
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.sh`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 138
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 138
   ```
