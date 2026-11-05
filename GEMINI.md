# OmniVim AI Pair-Programming Guidelines & Agent Memory

이 프로젝트의 표준 AI 가이드라인은 [AGENTS.md](AGENTS.md) 및 [PRACTICE_GUIDE.md](PRACTICE_GUIDE.md)에 기술되어 있습니다.

- **사용법/실습방법 질의 ("어떻게 사용하지?", "어떻게 해야해?", "실습 순서 알려줘")**:
  1. 팁을 검색/선택한다 (`practice` 또는 `practice -i` -> fzf 대화형 검색창)
  2. 선호하는 에디터로 연다 (`practice <번호> [--vim | --nvim | --code | --clion | --pycharm | --idea]`)
  3. 손으로 직접 타이핑한다 (`practice.*` 편집 후 `:w` 저장)
  4. 0.1초 만에 자동 채점한다 (`check <번호>` -> 🟢 `[ PASS ]` 또는 🔴 `[ FAIL ]` Unified Diff 대조)
  5. 원본 파일로 복원하거나 다음 팁으로 넘어간다 (`reset <번호>` 또는 `reset --all`)
  6. JetBrains IDE에서 설정 핫 리로드가 필요할 때는 재부팅하지 않고 `:source ~/.ideavimrc`를 실행한다
