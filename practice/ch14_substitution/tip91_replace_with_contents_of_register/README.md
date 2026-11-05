# Tip 91: Replace with Contents of Register

> **출처**: 《Practical Vim, Second Edition》 p. 219  
> **챕터**: Substitution (ch14_substitution)

---

## 🎯 Concept (학습 목표)
:%s/pattern/\=@0/g 로 0번 레지스터에 복사해 둔 텍스트를 치환값으로 주입합니다.

---

## 📝 Mission (실습 미션)
yiw 후 :s/replace_me/\=@0/ 로 치환하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`yiw` `:` `s/replace_me/\=@0/<CR>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 91
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 91
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 91
   ```
