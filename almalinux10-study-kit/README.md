# AlmaLinux 10 / LinuxZoo Study Kit

A **community-created, unofficial** study companion for [LinuxZoo](https://linuxzoo.net/). Original notes and exercises, not a mirror or answer key.

## Start here

1. Open `tools/study.html` in a browser (offline flashcards, quiz, score and lesson filter).
2. Follow `STUDY_PLAN.md` for a four-week revision plan.
3. Use `CHEATSHEET.md` while practising in a LinuxZoo AlmaLinux 10 VM.
4. Read each Markdown note in `notes/`, perform the suggested lab and record observations.
5. Run `python3 tools/quiz.py` for terminal revision. Requires only standard Python.

LinuxZoo says to register/login, join queue, switch on and connect to the VM. The AlmaLinux 10 image uses `alice` for introductory practicals. Follow the site's current credentials and access instructions rather than storing credentials in this repo.

**Important:** On the homepage, fwall, diag, Apache1, Apache2 and Mail appear struck through. Links may still exist, but availability/assessment may vary. Don't assume tooling (`firewall-cmd`, `procmail`, etc.) is installed; compare the exact task with your live VM. Several admin commands require sudo.

## Contents

- `notes/`: 18 lesson notes, command examples, hands-on exercises, pitfalls and a note template
- `CHEATSHEET.md`: quick command lookup by topic
- `STUDY_PLAN.md`: four-week plan and active-recall method
- `TROUBLESHOOTING.md`: debugging decision tree and safe working habits
- `practice/`: progressive, independent exercises
- `tools/study.html`: standalone browser-based practice application
- `tools/quiz.py`: offline terminal quiz
- `data/flashcards.json`: editable question bank
- `data/lessons.json`: source tutorial index

## Uploading to your own GitHub repository

```bash
git init
git add .
git commit -m "Add LinuxZoo AlmaLinux 10 study kit"
# Option A: create a repository on GitHub and add its URL
git remote add origin https://github.com/YOUR-USERNAME/almalinux10-study-kit.git
git branch -M main
git push -u origin main
# Option B: with GitHub CLI installed and authenticated
# gh repo create almalinux10-study-kit --private --source=. --push
```

Created October 2026. Commands illustrate Linux administration; privileged or security-related changes should only be run inside your own permitted lab VM. No destructive automation is provided.
