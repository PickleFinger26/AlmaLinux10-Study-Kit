# 10 — SELinux Administration (`SELinux1`)

**Official tutorial:** https://linuxzoo.net/page/alma10/10-selinux1.html

**Core concepts:** SELinux mode, contexts, rules, ports and transitions.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. getenforce
# 2. sestatus
# 3. ls -Z /etc/rsyslog.conf
# 4. ps -eZ | grep rsyslog
# 5. ls -lZ /etc
# 6. sudo semanage port -l
# 7. sesearch -A -s syslogd_t -c file
# 8. sudo ausearch -m AVC -ts recent
# 9. ls /sys/fs/selinux
```

## Practical challenge

Split a context into user:role:type:level; inspect file/process contexts, search allow rules and check port labels.

## Common pitfall

SELinux type enforcement is separate from Unix permissions; do not disable it to solve a labeling error.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
