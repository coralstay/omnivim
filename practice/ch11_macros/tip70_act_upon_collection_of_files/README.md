# Tip 70: Act Upon a Collection of Files with :argdo normal @a

> **출처**: 《Practical Vim, Second Edition》 p. 167  
> **챕터**: Macros (ch11_macros)

---

## 🎯 Concept (학습 목표)
:argdo normal @a 로 열려있는 수십 개의 파일에 매크로를 일괄 적용합니다.

---

## 📝 Mission (실습 미션)
:s/draft/final/<CR> 로 컬렉션 설정을 갱신하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`:s/draft/final/<CR>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 70
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 70
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 70
   ```
