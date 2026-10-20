# 15 — HTTP Server (`Apache1`)

**Official tutorial:** https://linuxzoo.net/page/alma10/15-apache1.html

**Core concepts:** Apache httpd, UserDir, virtual hosts and SELinux.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. sudo systemctl start httpd
# 2. sudo systemctl reload httpd
# 3. sudo apachectl configtest
# 4. httpd -S
# 5. curl -I http://localhost/
# 6. getsebool httpd_read_user_content
# 7. sudo setsebool -P httpd_read_user_content on
# 8. ls -Zd /var/www/html
# 9. sudo restorecon -Rv /var/www/html
```

## Practical challenge

Serve a basic page, check virtual host selection, test UserDir and verify file permissions plus SELinux.

## Common pitfall

RHEL-like distributions use `httpd` service; use reload after syntax testing when possible.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
