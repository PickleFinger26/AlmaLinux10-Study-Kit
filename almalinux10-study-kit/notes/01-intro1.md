# 01 — Shell 101 (`intro1`)

**Official tutorial:** https://linuxzoo.net/page/alma10/01-intro1.html

**Core concepts:** Shell navigation, calendars and file operations.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. pwd
# 2. ls -la
# 3. cal 12 2002
# 4. cal 2005 > yearfile
# 5. date >> thismonth
# 6. cp source copy
# 7. mv old new
# 8. rm unwanted
# 9. cat a b c > combined
# 10. more combined
```

## Practical challenge

Practice in /home/alice: generate a calendar, redirect to a file, append a date, duplicate and rename files, concatenate them in order.

## Common pitfall

`>` overwrites, `>>` appends. `rm` removes without a recycle bin; inspect paths first.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
