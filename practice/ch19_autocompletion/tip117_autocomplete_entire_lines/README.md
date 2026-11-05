# Tip 117: Autocomplete Entire Lines with <C-x><C-l>

> **출처**: 《Practical Vim, Second Edition》 p. 290  
> **챕터**: Dial X for Autocompletion (ch19_autocompletion)

---

## 🎯 Concept (학습 목표)
<C-x><C-l> 단축키는 단어 단위가 아닌 Line (행 전체)을 다른 버퍼나 이전 코드에서 매칭하여 일괄 복제 입력합니다.

---

## 📝 Mission (실습 미션)
둘째 줄의 System. 뒤에서 <C-x><C-l>을 눌러 첫 줄의 로깅 코드를 통째로 완성하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`GA` `<C-x>` `<C-l>` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.java`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.java`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 117
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.java`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 117
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 117
   ```
