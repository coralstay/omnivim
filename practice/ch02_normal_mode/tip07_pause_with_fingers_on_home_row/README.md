# Tip 7: Pause with Your Fingers on the Home Row

> **출처**: 《Practical Vim, Second Edition》 p. 17  
> **챕터**: Normal Mode (ch02_normal_mode)

---

## 🎯 Concept (학습 목표)
노멀 모드는 Vim의 Home (기본 상태)입니다. 편집을 마친 즉시 Esc로 노멀 모드로 복귀하는 습관을 들입니다.

---

## 📝 Mission (실습 미션)
단어를 수정한 뒤 즉시 Esc를 눌러 노멀 모드로 대기하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`cw` `edited` `<Esc>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 7
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 7
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 7
   ```
