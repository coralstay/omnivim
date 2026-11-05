# Tip 34: Run Shell Commands with :!

> **출처**: 《Practical Vim, Second Edition》 p. 70  
> **챕터**: Command-Line Mode (ch05_cmdline_mode)

---

## 🎯 Concept (학습 목표)
:!{cmd}로 외부 셸 명령을 실행하고, :read !{cmd}로 출력을 버퍼로 읽어옵니다.

---

## 📝 Mission (실습 미션)
:%!sort<CR> 로 외부 셸 sort 명령어를 적용하여 단어를 정렬하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`:%!sort<CR>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 34
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 34
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 34
   ```
