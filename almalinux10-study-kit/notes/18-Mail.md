# 18 — Procmail configuration (`Mail`)

**Official tutorial:** https://linuxzoo.net/page/alma10/18-email.html

**Core concepts:** Mail processing and basic filtering (legacy tutorial).

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. man procmail
# 2. ls -la ~/.procmailrc
# 3. grep -n "^:" ~/.procmailrc
# 4. systemctl status postfix
# 5. journalctl -u postfix -n 30
# 6. mailq
```

## Practical challenge

Read sample procmail recipes and explain their matching and delivery actions; do not use real mailboxes.

## Common pitfall

Legacy/struck-through lesson; procmail is not necessarily installed or recommended for new deployments.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
