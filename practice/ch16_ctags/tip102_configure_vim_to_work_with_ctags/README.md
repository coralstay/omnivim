# Tip 102: Configure Vim to Work with Ctags

> **출처**: 《Practical Vim, Second Edition》 p. 247  
> **챕터**: Index & Navigate with Ctags (ch16_ctags)

---

## 🎯 Concept (학습 목표)
:set tags=./tags;,tags 로 상위 디렉터리까지 tags 파일을 자동으로 탐색하게 설정합니다.

---

## 📝 Mission (실습 미션)
:s/disabled/enabled/<CR> 로 태그 설정을 활성화하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`:s/disabled/enabled/<CR>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 102
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 102
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 102
   ```
