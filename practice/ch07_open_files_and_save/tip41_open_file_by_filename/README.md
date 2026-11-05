# Tip 41: Open a File by Filename Using :find

> **출처**: 《Practical Vim, Second Edition》 p. 93  
> **챕터**: Open Files and Save (ch07_open_files_and_save)

---

## 🎯 Concept (학습 목표)
:set path+=** 설정 후 :find {filename} 으로 프로젝트 어디든 즉시 엽니다.

---

## 📝 Mission (실습 미션)
:s/target_file/found_file/<CR> 로 파일명을 갱신하세요.

### ⌨️ Recommended Keys (권장 키 입력 시퀀스):
> **`:s/target_file/found_file/<CR>`**

---

## 📂 실습 파일 안내
- **`practice.txt`**: 사용자가 직접 편집할 원본 대상 파일입니다.
- **`expected_practice.txt`**: 실습 완료 후 나와야 하는 정답 파일입니다.

### 🚀 실습 진행 방법
1. 터미널에서 아래 명령을 실행하여 이 실습 파일을 편집기로 엽니다:
   ```bash
   ./scripts/practice.sh 41
   ```
2. 위의 권장 키 입력 시퀀스를 참고하여 `practice.txt`을 수정하고 저장합니다 (`:w`).
3. 아래 명령을 실행하여 정답과 일치하는지 채점합니다:
   ```bash
   ./scripts/check.sh 41
   ```
4. 언제든 처음 상태로 되돌리려면 아래 명령을 실행합니다:
   ```bash
   ./scripts/reset.sh 41
   ```
