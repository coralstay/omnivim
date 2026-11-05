# Tip 137: Drill 03: Run and Debug Test in Isolation

> **출처**: 《Practical Vim, Second Edition》 Keymap Drill #3  
> **챕터**: Cross-IDE Situational Keymap Drills (ch22_ide_keymap_drills)

---

## 🎯 Concept (학습 목표)
RunClass (<Space>rc: 단일 테스트 격리 실행) 및 DebugClass (<Space>dc: 디버그 모드 구동)를 조합하여 테스트 주도 개발 사이클을 가속합니다.

---

## 📝 Mission (실습 미션)
실패하는 테스트의 예상 값 400 을 200 으로 교체하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`jj0f4cw200<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.test.js`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.test.js`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 137
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.test.js`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 137
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 137
   ```
