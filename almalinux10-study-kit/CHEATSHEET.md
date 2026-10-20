# AlmaLinux 10 command cheat sheet

> These are examples, not guaranteed answers to LinuxZoo graded questions. Replace placeholder names and paths. Commands affecting security or services belong in your own VM.

## Permission octal reference

| Octal | Bits | Meaning |
|---|---|---|
| 0 | --- | none |
| 1 | --x | execute/traverse |
| 2 | -w- | write |
| 3 | -wx | write + execute |
| 4 | r-- | read |
| 5 | r-x | read + execute |
| 6 | rw- | read + write |
| 7 | rwx | all |

Examples: `644 = rw-r--r--`, `640 = rw-r-----`, `750 = rwxr-x---`, `755 = rwxr-xr-x`.

**Symbolic:** `u` owner, `g` group, `o` others, `a` all; `+`, `-`, `=` change modes.

**Redirection:** `>` replace, `>>` append, `2>` error output, `|` pipe.

---

## Shell and files

| Command | What it does |
|---|---|
| `pwd` | Print current directory |
| `ls -la` | Show all entries and detailed permissions |
| `cd ~` | Go home |
| `mkdir -p a/b` | Create nested directories |
| `cp -i source destination` | Copy, prompting before overwriting |
| `mv -i old new` | Rename/move, prompting before overwriting |
| `rm -i file` | Remove a file with confirmation |
| `stat file` | Inspect size, ownership, times and permissions |
| `file name` | Detect file type |
| `cal 12 2002` | Display calendar for December 2002 |

## Globbing and searching

| Command | What it does |
|---|---|
| `ls *.txt` | Match names ending in .txt |
| `ls file?.txt` | Single-character placeholder |
| `ls file[12].txt` | Match listed characters |
| `find . -type f -name "*.log"` | Recursively find log files |
| `grep -Rni "error" .` | Recursive case-insensitive search with line numbers |
| `which ssh` | Locate executable in PATH |

## Pipes and redirection

| Command | What it does |
|---|---|
| `cmd > output` | Overwrite output |
| `cmd >> output` | Append output |
| `cmd 2> error.log` | Redirect error output |
| `cmd1 \| cmd2` | Pipe stdout |
| `head -n 5000 words \| tail -n 1` | Extract line 5000 |
| `sort file \| uniq -c \| sort -nr` | Frequency sort |
| `wc -l file` | Count newline-terminated lines |
| `tail -f /var/log/messages` | Follow a growing log file |
| `tee output` | Display and save pipeline input |

## Permissions

| Command | What it does |
|---|---|
| `ls -l file` | Read owner/group/other permissions |
| `chmod 640 file` | Owner rw; group r; others none |
| `chmod 750 script` | Owner rwx; group rx; others none |
| `chmod u+x script` | Add execute for owner |
| `chmod g-w file` | Remove group write |
| `chown user:group file` | Change owner/group (normally root) |
| `umask` | Display creation-mask settings |
| `id; groups` | Show current user and group memberships |

## vi quick keys

| Command | What it does |
|---|---|
| `i` | Enter insert mode |
| `Esc` | Return to normal mode |
| `:wq` | Write and exit |
| `:q!` | Quit without saving |
| `dd` | Delete current line |
| `yy` | Yank current line |
| `p` | Paste after cursor |
| `/word` | Search forward |
| `n` | Next match |
| `u` | Undo |

## Processes and storage

| Command | What it does |
|---|---|
| `ps aux` | Processes with details |
| `ps -ef` | Full process list |
| `pgrep -a rsyslogd` | Find PID and command |
| `kill -TERM PID` | Request graceful process termination |
| `lsblk -f` | Block devices and filesystems |
| `df -h` | Filesystem usage |
| `du -sh DIRECTORY` | Directory size |
| `sudo pvdisplay` | LVM physical volumes |
| `sudo vgdisplay` | LVM volume groups |
| `sudo lvdisplay` | LVM logical volumes |
| `cat /proc/swaps` | Swap allocations |
| `findmnt /` | Show root mount |

## Services and logs

| Command | What it does |
|---|---|
| `systemctl status rsyslog` | Service status |
| `systemctl cat rsyslog` | Read unit definition |
| `sudo systemctl start httpd` | Start service now |
| `sudo systemctl reload httpd` | Reload service configuration |
| `sudo systemctl enable mariadb` | Enable service at boot |
| `sudo systemctl disable mariadb` | Disable boot activation |
| `journalctl -u httpd -n 50` | Recent service journal |
| `journalctl -p err -b` | Errors since boot |
| `systemctl --failed` | List failed units |

## Networking and DNS

| Command | What it does |
|---|---|
| `ip -br a` | Brief interface addresses |
| `ip route` | Routes and gateway |
| `ip -4 addr` | IPv4 addresses and prefix |
| `nmcli device status` | NetworkManager devices |
| `ss -lntup` | Listening TCP/UDP sockets |
| `ping -c 3 127.0.0.1` | Check local IP stack |
| `dig example.org A` | Query A record |
| `dig example.org MX` | Query MX record |
| `dig @127.0.0.1 example.org` | Query chosen DNS server |
| `named-checkconf` | Validate named config |
| `named-checkzone example.test zonefile` | Validate DNS zone |

## SELinux

| Command | What it does |
|---|---|
| `getenforce` | Current SELinux mode |
| `sestatus` | Detailed SELinux status |
| `ls -Z file` | File SELinux context |
| `ps -eZ` | Process SELinux contexts |
| `matchpathcon PATH` | Expected file context |
| `sudo restorecon -v PATH` | Apply default file context |
| `sudo semanage fcontext -l` | Persistent file label mappings |
| `sudo semanage port -l` | Port type mappings |
| `getsebool -a` | List policy booleans |
| `sudo setsebool -P BOOLEAN on` | Set boolean persistently |
| `sudo ausearch -m AVC -ts recent` | Recent access denials |

## Firewall and web

| Command | What it does |
|---|---|
| `sudo nft list ruleset` | Display nftables rules |
| `sudo iptables -S` | Display iptables rules |
| `sudo firewall-cmd --list-all` | Show firewalld zone config (if available) |
| `sudo apachectl configtest` | Check Apache config syntax |
| `httpd -S` | Display Apache virtual host map |
| `curl -I http://localhost/` | Fetch response headers |
| `curl -u user http://localhost/private/` | Test HTTP basic auth over a trusted lab connection |
| `htpasswd -c users.htpasswd user` | Create an auth file (initial creation only) |
| `getsebool httpd_read_user_content` | Inspect UserDir SELinux boolean |

## Troubleshooting flow

`id` → `ls -l` → `ls -Z` → `systemctl status SERVICE` → `journalctl -u SERVICE` → `ss -lntup` → application syntax test.
