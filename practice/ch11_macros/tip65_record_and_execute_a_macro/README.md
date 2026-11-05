# Tip 65: Record and Execute a Macro

> **출처**: 《Practical Vim, Second Edition》 p. 155  
> **챕터**: Macros (ch11_macros)

---

## 🎯 Concept (학습 목표)
qa 로 녹화를 시작하고 작업을 수행한 뒤 q 로 마치고, @a 로 재생합니다.

---

## 📝 Mission (실습 미션)
:%normal I* <CR> 로 목록에 마크다운 기호를 일괄 추가하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`:%normal I* <CR>`**

---

## 📂 실습 파일 안내
- **`practice.md`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.md`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 65
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.md`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 65
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 65
   ```
