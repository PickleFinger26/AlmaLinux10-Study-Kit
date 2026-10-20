# Troubleshooting playbook

1. **What changed?** Reproduce the error; capture the exact command and stderr.
2. **Who am I?** `id`, `pwd`, `ls -la`, `sudo -l` when permitted.
3. **Does the file exist?** `stat PATH`, `namei -l PATH`, `file PATH`.
4. **Is the service active?** `systemctl status NAME`, `journalctl -u NAME -n 50 --no-pager`.
5. **Is the configuration valid?** Application-specific test, e.g. `apachectl configtest`, `named-checkconf`.
6. **Does it listen?** `ss -lntup`, `ip route`, `curl -v http://localhost/`, `dig @SERVER NAME`.
7. **Is security blocking access?** UNIX DAC (`ls -l`), SELinux (`ls -Z`, `getenforce`, `ausearch -m AVC -ts recent`) and firewall rules.
8. **Recheck.** Run the original test; record what changed and how you know it worked.

Avoid `chmod -R 777`, broad SELinux disablement, unreviewed `rm -rf`, flushing firewall rules, or restarting network services while connected over SSH.
