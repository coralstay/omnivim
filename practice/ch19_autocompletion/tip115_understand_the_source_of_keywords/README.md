# Tip 115: Understand the Source of Keywords

> **출처**: 《Practical Vim, Second Edition》 p. 285  
> **챕터**: Dial X for Autocompletion (ch19_autocompletion)

---

## 🎯 Concept (학습 목표)
'complete' Option (설정 옵션: set complete=.,w,b,u,t,i)을 통해 현재 버퍼(.), 창(w), 버퍼 목록(b), 태그(t) 등 키워드를 수집할 소스의 우선순위와 범위를 제어합니다.

---

## 📝 Mission (실습 미션)
auth 뒤에서 <C-n>을 눌러 상단 주석에 선언된 authenticate를 완성하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`GA` `<C-n>` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.js`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.js`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 115
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.js`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 115
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 115
   ```
