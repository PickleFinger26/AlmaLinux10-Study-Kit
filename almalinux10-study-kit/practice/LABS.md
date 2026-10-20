# Independent practice labs

Work in your own throwaway VM or `~/study-lab`; LinuxZoo graded questions often expect exact paths so follow its instructions there.

## Lab A — Shell detective (intro1 → pipe)
1. Make `~/study-lab/{in,out,tmp}`. Create `in/apple.txt`, `in/apricot.txt`, `in/banana.log`.
2. List only `.txt` names using globbing. Copy them to `out` without modifying originals.
3. Set the output files to `640`. Explain who can read each.
4. Create a file with 12 lines; print only line 7 using a pipeline.
5. Write the number of `.txt` files to `count.txt` with redirection.

## Lab B — Observation first (admin → net)
1. Record kernel release, root mount device, and default gateway.
2. Identify one active service and its main PID and unit file.
3. Find a listening TCP port and identify owning process if permitted.
4. Explain one reason `systemctl start` differs from `enable`.

## Lab C — Security layers (SELinux → Apache)
1. Inspect a file's UNIX mode and SELinux context.
2. Predict why a readable file might still be denied to httpd.
3. Run Apache's syntax check in an environment where Apache is installed.
4. Diagnose one mock 403 error using DAC, contexts, and log evidence.

## Lab D — Operational troubleshooting (DNS → logs)
1. Query A and MX records with `dig`; describe the different response records.
2. Find service warning entries for the current boot.
3. Explain the difference among 401, 403, 404, and 500 HTTP responses.
4. Write a five-line incident report: symptom, checks, evidence, correction, verification.
