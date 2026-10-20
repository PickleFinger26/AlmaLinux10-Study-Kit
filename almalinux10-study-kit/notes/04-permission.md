# 04 — Permissions (`permission`)

**Official tutorial:** https://linuxzoo.net/page/alma10/04-intro4.html

**Core concepts:** Owner/group/other, rwx, octal and symbolic chmod.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. ls -l file
# 2. stat -c "%a %A %U %G" file
# 3. chmod 750 script.sh
# 4. chmod u+x script.sh
# 5. chmod g-w file
# 6. chmod o=r file
# 7. id
# 8. groups
# 9. umask
```

## Practical challenge

Translate `rwxr-x---` to 750; assign owner rwx, group rx, others none in a practice directory.

## Common pitfall

For a directory x means traversal and r means listing. Permission priority is owner, then group, then other.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
