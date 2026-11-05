# Tip 75: Use the \V Switch for Verbatim Search

> **출처**: 《Practical Vim, Second Edition》 p. 182  
> **챕터**: Matching Patterns (ch12_matching_patterns)

---

## 🎯 Concept (학습 목표)
/\V (Very Nomagic) 스위치는 마침표나 별표 등 모든 특수문자를 순수 문자 그대로 검색합니다.

---

## 📝 Mission (실습 미션)
:%s/\Va.k.a./also known as/g<CR> 로 리터럴 점을 포함한 문자열을 치환하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`:%s/\Va.k.a./also known as/g<CR>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 75
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 75
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 75
   ```
