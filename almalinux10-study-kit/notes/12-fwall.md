# 12 — Firewalls (`fwall`)

**Official tutorial:** https://linuxzoo.net/page/alma10/12-fwall.html

**Core concepts:** Packet filtering, rules, ports and verification.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. sudo firewall-cmd --state
# 2. sudo firewall-cmd --get-active-zones
# 3. sudo firewall-cmd --list-all
# 4. sudo firewall-cmd --add-service=http
# 5. sudo firewall-cmd --permanent --add-service=http
# 6. sudo firewall-cmd --reload
# 7. sudo nft list ruleset
# 8. sudo iptables -S
```

## Practical challenge

Inspect current rules; in a disposable VM allow HTTP temporarily, then confirm the rule and clean up.

## Common pitfall

LinuxZoo firewall tutorial may use iptables rather than firewalld; follow the actual VM instructions, and avoid locking out SSH.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
