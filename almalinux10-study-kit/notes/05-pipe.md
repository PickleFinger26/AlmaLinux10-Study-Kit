# 05 — Pipes (`pipe`)

**Official tutorial:** https://linuxzoo.net/page/alma10/05-intro5.html

**Core concepts:** Pipelines, redirection, filters and text processing.

## Working notes

- First predict what a command will do, then run it in your **LinuxZoo AlmaLinux 10 VM**.
- Read unfamiliar syntax with `man COMMAND` or `COMMAND --help`.
- For questions that ask about your current VM, collect the answer from that VM rather than copying fixed answers.

## Command examples

```bash
# 1. cat file | sort | uniq -c
# 2. grep -i "error" app.log
# 3. grep -n "word" file
# 4. head -n 10 file
# 5. tail -n 10 file
# 6. head -n 5000 words | tail -n 1
# 7. wc -l file
# 8. sort file | uniq
# 9. command 2> errors.txt
```

## Practical challenge

Use `head -n 5000 words | tail -n 1` to isolate line 5000; count repeated entries in a text file.

## Common pitfall

`|` sends stdout to the next command; `2>` redirects stderr; `tee` can save and display.

## Retrieval prompts

1. What is the purpose of each flag in the key commands above?
2. Which command would you use to verify the result, without assuming it worked?
3. What would fail without sufficient permissions or correct environment setup?

## My lab notes

- **Commands I tested:**
- **What happened:**
- **Mistake / fix:**
- **Confidence (1–5):**
