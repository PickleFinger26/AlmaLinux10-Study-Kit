# 07 — Essential Unix Commands (`essential`)

**Official tutorial:** https://linuxzoo.net/page/alma10/07-essential.html

**Core concepts:** Finding files, processes and systems information.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. man find
# 2. which bash
# 3. type cd
# 4. find /etc -name "*.conf" 2>/dev/null
# 5. grep -Rni "listen" /etc 2>/dev/null
# 6. ps aux
# 7. df -h
# 8. du -sh ~
# 9. free -h
# 10. uname -a
# 11. hostnamectl
# 12. tar -czf archive.tgz folder
```

## Practical challenge

Locate config files, compare disk versus directory usage, and archive a practice folder.

## Common pitfall

Avoid unrestricted recursive searches on a production machine; `/etc` may require permissions.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
