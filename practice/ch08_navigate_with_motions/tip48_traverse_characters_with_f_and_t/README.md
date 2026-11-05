# Tip 48: Traverse Characters with f and t

> **출처**: 《Practical Vim, Second Edition》 p. 111  
> **챕터**: Motions & Text Objects (ch08_navigate_with_motions)

---

## 🎯 Concept (학습 목표)
f{char}(해당 문자), t{char}(문자 앞)로 행 내 초고속 이동 후 ; 과 , 로 반복합니다.

---

## 📝 Mission (실습 미션)
f; 로 세미콜론 위치로 이동한 뒤 r, 로 쉼표로 교체하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`f;r,`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 48
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 48
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 48
   ```
