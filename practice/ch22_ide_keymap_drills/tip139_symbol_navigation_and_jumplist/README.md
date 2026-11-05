# Tip 139: Drill 05: Symbol Navigation and Jump List Traversal

> **출처**: 《Practical Vim, Second Edition》 Keymap Drill #5  
> **챕터**: Cross-IDE Situational Keymap Drills (ch22_ide_keymap_drills)

---

## 🎯 Concept (학습 목표)
GotoDeclaration (gd: 선언부 이동) 및 GotoImplementation (gi: 구현체 이동) 후, Jump List Return (<C-o>: 점프 리스트 복귀)으로 직전 편집 위치로 복귀합니다.

---

## 📝 Mission (실습 미션)
호출부에서 구형 식별자 legacyFetchUser 를 fetchUserById 로 변경하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`G0flcwfetchUserById<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.js`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.js`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 139
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.js`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 139
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 139
   ```
