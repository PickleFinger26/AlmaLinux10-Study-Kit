# 16 — Basic Authentication (`Apache2`)

**Official tutorial:** https://linuxzoo.net/page/alma10/16-apache2.html

**Core concepts:** HTTP basic auth, password files and access restrictions.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. htpasswd -c /etc/httpd/.htpasswd student
# 2. htpasswd /etc/httpd/.htpasswd second
# 3. sudo apachectl configtest
# 4. curl -I http://localhost/private/
# 5. curl -u student http://localhost/private/
# 6. sudo journalctl -u httpd -n 30
```

## Practical challenge

Configure authentication for a private test directory, test a 401 response, then authenticated access.

## Common pitfall

Basic auth must run over HTTPS for confidentiality; do not commit `.htpasswd` or passwords.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
