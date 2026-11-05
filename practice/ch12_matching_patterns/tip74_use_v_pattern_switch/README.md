# Tip 74: Use the \v Pattern Switch for Regexes

> **출처**: 《Practical Vim, Second Edition》 p. 179  
> **챕터**: Matching Patterns (ch12_matching_patterns)

---

## 🎯 Concept (학습 목표)
/\v (Very Magic) 스위치를 켜면 역슬래시 이스케이프 없이 현대 정규표현식 문법으로 검색합니다.

---

## 📝 Mission (실습 미션)
:%s/\v#([0-9a-f]{6})/color:#\1/g<CR> 로 색상 코드를 변환하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`:%s/\v#([0-9a-f]{6})/color:#\1/g<CR>`**

---

## 📂 실습 파일 안내
- **`practice.css`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.css`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 74
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.css`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 74
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 74
   ```
