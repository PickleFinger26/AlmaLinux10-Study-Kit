# 17 — Basic File Handling (`log`)

**Official tutorial:** https://linuxzoo.net/page/alma10/17-log.html

**Core concepts:** Log scanning, text extraction and pipelines.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. journalctl -u httpd --since today
# 2. tail -n 50 /var/log/messages
# 3. grep -Ei "warn|error" app.log
# 4. awk "{print \$1}" access.log | sort | uniq -c | sort -nr | head
# 5. sed -n "1,20p" file
# 6. cut -d: -f1 /etc/passwd
```

## Practical challenge

Find top source addresses in a demo access log and count log event types.

## Common pitfall

Log formats differ; ensure your awk column choice matches the file. Some logs need sudo.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
