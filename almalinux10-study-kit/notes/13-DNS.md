# 13 — DNS named (`DNS`)

**Official tutorial:** https://linuxzoo.net/page/alma10/13-dns.html

**Core concepts:** DNS querying, records, BIND configuration and validation.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. dig example.com A
# 2. dig example.com MX
# 3. dig @127.0.0.1 example.com
# 4. host example.com
# 5. resolvectl status
# 6. named-checkconf
# 7. named-checkzone example.test /var/named/example.test.zone
# 8. systemctl status named
# 9. journalctl -u named -n 30
```

## Practical challenge

Identify A, AAAA, NS, MX, CNAME and PTR roles; validate a lab zone before restarting named.

## Common pitfall

Use the correct nameserver/zone for your lab; BIND uses `named`, not `httpd`.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
