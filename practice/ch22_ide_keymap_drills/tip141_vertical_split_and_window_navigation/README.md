# Tip 141: Drill 07: Vertical Window Split and Focus Navigation

> **출처**: 《Practical Vim, Second Edition》 Keymap Drill #7  
> **챕터**: Cross-IDE Situational Keymap Drills (ch22_ide_keymap_drills)

---

## 🎯 Concept (학습 목표)
SplitVertically (<Space>sv: 수직 분할)로 에디터를 분할하고, Window Navigation (<C-l>/<C-h>: 좌우 분할 창 이동) 후 Close Content (<Space>sc: 분할 닫기)로 정리합니다.

---

## 📝 Mission (실습 미션)
좌우 분할 동기화 확인을 위해 파일 끝에 // Split view synced 를 추가하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`Go// Split view synced<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 141
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 141
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 141
   ```
