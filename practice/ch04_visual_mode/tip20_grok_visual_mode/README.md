# Tip 20: Grok Visual Mode

> **출처**: 《Practical Vim, Second Edition》 p. 41  
> **챕터**: Visual Mode (ch04_visual_mode)

---

## 🎯 Concept (학습 목표)
v(문자), V(줄), <C-v>(블록) 세 가지 시각 모드의 특성을 이해합니다.

---

## 📝 Mission (실습 미션)
V 키로 줄 전체를 선택 후 d로 삭제하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`V` `d`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 20
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 20
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 20
   ```
