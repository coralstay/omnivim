# Tip 66: Normalize, Strike, Abort in Macros

> **출처**: 《Practical Vim, Second Edition》 p. 158  
> **챕터**: Macros (ch11_macros)

---

## 🎯 Concept (학습 목표)
매크로의 시작 위치를 항상 일관되게 Normalize (0번 컬럼 정규화, 예: 0 또는 ^)하는 원칙을 지킵니다.

---

## 📝 Mission (실습 미션)
0 키로 커서를 줄 맨 앞으로 정규화하며 매크로를 작성하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`qa` `0` `x` `q`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 66
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 66
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 66
   ```
