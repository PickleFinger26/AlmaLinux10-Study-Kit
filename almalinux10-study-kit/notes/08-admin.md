# 08 — Essential Unix Administration (`admin`)

**Official tutorial:** https://linuxzoo.net/page/alma10/08-admin.html

**Core concepts:** LVM, block devices, processes, systemd services.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. sudo sfdisk -l /dev/sda
# 2. sudo pvdisplay
# 3. sudo vgdisplay
# 4. sudo lvdisplay
# 5. lsblk -f
# 6. cat /etc/fstab
# 7. cat /proc/swaps
# 8. ps aux | grep rsyslog
# 9. systemctl status rsyslog
# 10. systemctl cat rsyslog
# 11. sudo systemctl start mariadb
# 12. sudo systemctl enable mariadb
# 13. sudo systemctl disable mariadb
```

## Practical challenge

Identify PV/VG/LV and filesystem UUID on your VM; inspect rsyslog unit and MariaDB service state.

## Common pitfall

Inspect before changing services or mounts. Enabling controls boot behavior; starting controls running state.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
