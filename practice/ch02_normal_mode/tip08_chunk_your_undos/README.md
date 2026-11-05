# Tip 8: Chunk Your Undos

> **출처**: 《Practical Vim, Second Edition》 p. 18  
> **챕터**: Normal Mode (ch02_normal_mode)

---

## 🎯 Concept (학습 목표)
Undo(u) 단위를 고려하여 삽입 모드 진입과 탈출을 계획합니다.

---

## 📝 Mission (실습 미션)
한 문장 단위로 Insert 모드를 나갔다 들어와서 u 실행 시 한 번에 취소되는 단위를 확인하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`o` `Sentence one.` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 8
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 8
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 8
   ```
