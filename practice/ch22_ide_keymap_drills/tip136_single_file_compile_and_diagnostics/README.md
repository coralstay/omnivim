# Tip 136: Drill 02: Single File Compile and Diagnostics Traversal

> **출처**: 《Practical Vim, Second Edition》 Keymap Drill #2  
> **챕터**: Cross-IDE Situational Keymap Drills (ch22_ide_keymap_drills)

---

## 🎯 Concept (학습 목표)
CompileDirty (<Space>cc: 단일 파일 컴파일)로 수정한 파일만 독립 컴파일하고, Diagnostics (진단 라인: ]d / [d)으로 에러 위치를 고속 순회합니다.

---

## 📝 Mission (실습 미션)
문법 오류가 있는 retrun 을 return 으로 수정하고 라인 끝에 세미콜론을 추가하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`j0wciwreturn<Esc>A;<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.ts`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.ts`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 136
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.ts`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 136
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 136
   ```
