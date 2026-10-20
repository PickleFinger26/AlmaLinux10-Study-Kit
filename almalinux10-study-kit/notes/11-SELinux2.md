# 11 — SELinux Usage (`SELinux2`)

**Official tutorial:** https://linuxzoo.net/page/alma10/11-selinux2.html

**Core concepts:** Changing SELinux labels, policy mappings and booleans.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. ls -Zd ~/secure
# 2. sudo chcon -t etc_t ~/protect
# 3. matchpathcon ~/protect/test2
# 4. sudo semanage fcontext -l
# 5. sudo semanage fcontext -a -t bin_t "/home/alice/.*\.bin"
# 6. sudo restorecon -v ~/test.bin
# 7. getsebool httpd_tmp_exec
# 8. sudo setsebool -P httpd_tmp_exec on
```

## Practical challenge

Compare labels after creating, copying and moving files; inspect matchpathcon; practice temporary vs persistent context rules.

## Common pitfall

`chcon` can be reset by `restorecon`; persistent labeling uses `semanage fcontext` plus `restorecon`.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
