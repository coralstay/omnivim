# Tip 142: Drill 08: Delimiter and Text Object Modification with Surround

> **출처**: 《Practical Vim, Second Edition》 Keymap Drill #8  
> **챕터**: Cross-IDE Situational Keymap Drills (ch22_ide_keymap_drills)

---

## 🎯 Concept (학습 목표)
Change Surrounding (cs"' : 큰따옴표를 작은따옴표로 교체), Delete Surrounding (ds" : 구분자 삭제), Yank Surround (ysiw] : 단어를 대괄호로 감싸기)를 수행합니다.

---

## 📝 Mission (실습 미션)
첫 줄의 Quote Replacement (따옴표 교체: cs"'), 둘째 줄의 Delimiter Deletion (구분자 삭제: ds"), 셋째 줄 Surround with Brackets (대괄호 감싸기: ysiw])를 수행하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`cs"'jds"jysiw]`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 142
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 142
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 142
   ```
