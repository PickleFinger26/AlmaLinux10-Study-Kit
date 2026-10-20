# 02 — Directories (`intro2`)

**Official tutorial:** https://linuxzoo.net/page/alma10/02-intro2.html

**Core concepts:** Absolute/relative paths, directory trees and moving around.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. pwd
# 2. cd ~
# 3. cd ..
# 4. cd -
# 5. mkdir -p work/{progs,tutorial,misc}
# 6. mkdir letters scripts
# 7. rmdir emptydir
# 8. find . -maxdepth 3 -type d
# 9. ls -ld work
```

## Practical challenge

Build the directory tree `work/{progs,tutorial,misc}`, `letters`, `scripts`; travel using relative and absolute paths.

## Common pitfall

`rmdir` requires an empty directory; check `pwd` before destructive actions.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
