# Tip 106: Compile Code Without Leaving Vim with :make

> **출처**: 《Practical Vim, Second Edition》 p. 259  
> **챕터**: Quickfix List (ch17_quickfix)

---

## 🎯 Concept (학습 목표)
:make 로 에디터 내부에서 빌드를 실행하고 컴파일 에러를 즉시 파싱합니다.

---

## 📝 Mission (실습 미션)
3w 이동 후 ciw 로 syntax_err 를 valid_code 로 수정하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`3w` `ciwvalid_code<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 106
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 106
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 106
   ```
