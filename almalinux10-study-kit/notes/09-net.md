# 09 — Linux Networking (`net`)

**Official tutorial:** https://linuxzoo.net/page/alma10/09-net.html

**Core concepts:** Interfaces, addresses, routes and host troubleshooting.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. ip -br address
# 2. ip link
# 3. ip route
# 4. ip -4 addr show
# 5. ip -4 route
# 6. nmcli device status
# 7. nmcli connection show
# 8. ping -c 3 127.0.0.1
# 9. ss -tulpen
# 10. hostname -I
```

## Practical challenge

Find interface with 10.x address, broadcast address and CIDR prefix; identify default route and listening sockets.

## Common pitfall

CIDR /24 corresponds to 255.255.255.0; don't change remote network settings without recovery access.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
