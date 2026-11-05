# Tip 19: Overwrite Existing Text with Replace Mode

> **출처**: 《Practical Vim, Second Edition》 p. 37  
> **챕터**: Insert Mode (ch03_insert_mode)

---

## 🎯 Concept (학습 목표)
R 키로 Replace (교체) 모드에 진입하여 기존 텍스트를 덮어씁니다.

---

## 📝 Mission (실습 미션)
R 키를 누르고 'NEW'를 입력하여 기존 'OLD'를 덮어쓰세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`R` `NEW` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 19
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 19
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 19
   ```
