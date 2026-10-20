# 14 — Server Admin Tasks (`diag`)

**Official tutorial:** https://linuxzoo.net/page/alma10/14-diag.html

**Core concepts:** Diagnosis: services, resources, logs and sockets.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. uptime
# 2. top -b -n 1 | head
# 3. free -h
# 4. df -h
# 5. journalctl -p warning -b
# 6. systemctl --failed
# 7. ss -lntup
# 8. lsof -i
# 9. dmesg | tail
# 10. sudo du -sh /var/log/* 2>/dev/null
```

## Practical challenge

Find one failing service and collect status, recent logs, resource usage and bound ports.

## Common pitfall

Observe, form a hypothesis, then change one variable; capture logs before restarts.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
