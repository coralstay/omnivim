# Tip 135: Drill 01: Explorer and Editor Focus Navigation

> **출처**: 《Practical Vim, Second Edition》 Keymap Drill #1  
> **챕터**: Cross-IDE Situational Keymap Drills (ch22_ide_keymap_drills)

---

## 🎯 Concept (학습 목표)
ActivateProjectToolWindow (<Space>e: 프로젝트 탐색기 열기) 및 SelectInProjectView (<Space>ee: 현재 파일 위치 탐색) 후 FocusEditor (<Esc>: 에디터 포커스 복귀)를 수행합니다.

---

## 📝 Mission (실습 미션)
에디터 복귀 후 주석 라인 끝에 // Editor focus restored 를 추가하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`Go// Editor focus restored<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.js`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.js`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 135
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.js`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 135
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 135
   ```
