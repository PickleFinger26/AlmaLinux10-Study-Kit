# 03 — Wildcards (`wildcard`)

**Official tutorial:** https://linuxzoo.net/page/alma10/03-intro3.html

**Core concepts:** Shell globbing and filename matching.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. printf "%s\n" *.txt
# 2. ls file?.txt
# 3. ls data[123].csv
# 4. ls [[:upper:]]*
# 5. find . -name "*.log"
# 6. echo *.txt
```

## Practical challenge

Create sample .txt and .log files; predict which files `*`, `?`, and `[abc]` match before running commands.

## Common pitfall

Globs are expanded by the shell; quotes suppress expansion. Hidden dotfiles are often not matched by `*`.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
