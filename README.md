# DevOps Final Project — Notes Info Server

**Name:** [ahmed hani abuowda]
**Student ID:** [1320226477]
**Course:** Introduction to DevOps — Al-Aqsa University — Second Semester 2026
**Instructor:** Eng. Haneen Tabasi

## Project Description

This project is a small containerized web service called **Notes Info Server**.
It reports basic status information (a configurable greeting, the container's
hostname, and how many sample note files it can see) and exposes a health
endpoint. The project was built and version-controlled end-to-end following
the DevOps workflow taught in this course: Linux basics and Bash scripting,
Git version control, GitHub collaboration (branches + pull requests), a
custom multi-stage Docker image, and an automated CI pipeline with GitHub
Actions.

---

## Module 1 — Linux Basics

- `scripts/info.sh` — prints OS name/version, current user, date/time, and
  disk usage.
- `scripts/backup.sh` — copies all `.txt` files from `app/` into a `backup/`
  folder and prints how many files were copied.
- `logs/network.log` — output of the `ping` and `curl`/`wget` connectivity
  test (see Task 4).

**Screenshots:**
- [ ] `ls -R` output of the workspace structure
- [ ] `info.sh` execution output
- [ ] `backup.sh` execution output + `backup/` folder listing
- [ ] `logs/network.log` content via `cat`

---

## Module 2 — Git Version Control

Commit history shows:
1. Initial commit — project structure created
2. Three separate commits, each adding one `.txt` file to `app/`
3. A `feature/add-script` branch adding `scripts/hello.sh`, merged into `main`
4. A stage/unstage/diff demonstration (`git add`, `git restore --staged`, `git diff`)

**Screenshots:**
- [ ] `git log` after the initial commit
- [ ] `git log --oneline` after the 3 file commits
- [ ] `git log --oneline --graph` after the branch merge
- [ ] Staged state + `git diff` output

---

## Module 3 — GitHub — Remote Work

- Public repository: `devops-final-project`
- Branch `feature/github-setup` added `GITHUB_NOTES.md` and was merged via a
  Pull Request.
- Repository cloned into a separate folder to verify history and structure.

**Screenshots:**
- [ ] Repository files on GitHub after the first push
- [ ] `feature/github-setup` branch visible on GitHub
- [ ] Merged Pull Request confirmation page
- [ ] `git log --oneline` inside the freshly cloned copy

---

## Module 4 — Docker

**What does the image do?**
It runs a tiny Flask web app (`app/app.py`) that returns a JSON status page
at `/` (greeting message, hostname, note-file count, timestamp) and a
`/health` endpoint used for health checks.

**Why this base image (`python:3.12-slim`)?**
It's an official, actively maintained image with a small footprint compared
to the full `python` image, which keeps build times and final image size
down while still giving full pip/venv compatibility — no extra system
packages were needed for this app.

**Best practices applied (2+):**
1. **Multi-stage build** — dependencies are installed with `pip` in a
   `builder` stage; only the resulting packages are copied into the final
   image, so build tools never ship in the runtime image.
2. **Non-root user** — the container runs as `appuser`, not root
   (`USER appuser` in the Dockerfile).
3. **Environment-variable configuration** — `APP_MESSAGE` and `APP_PORT`
   change the app's behavior without touching any code.
4. **HEALTHCHECK** — Docker polls `/health` every 30s to detect if the app
   stops responding.

**How to build and run it:**
```bash
# from the project root (devops-final-project/)
docker build -f docker/Dockerfile -t yourname/notes-info-server:v1.0 .

docker run -d -p 5000:5000 \
  -e APP_MESSAGE="Hello from my DevOps project!" \
  --name notes-info-server \
  yourname/notes-info-server:v1.0

curl http://localhost:5000/
curl http://localhost:5000/health
docker images
```

**Screenshots:**
- [ ] `docker build` completing successfully
- [ ] `docker images` showing the tagged image
- [ ] `curl`/browser output proving the container runs correctly

---

## Module 5 — GitHub Actions (CI/CD)

The workflow at `.github/workflows/ci.yml` triggers on every push to `main`,
runs on `ubuntu-latest`, checks out the repository, and prints a greeting
plus a recursive file listing — a minimal smoke test confirming the
repository checks out correctly in a clean CI environment.

**Screenshot:**
- [ ] Successful (green ✅) run in the Actions tab

---

## Repository Structure

```
devops-final-project/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── notes1.txt, notes2.txt, notes3.txt
├── scripts/
│   ├── info.sh
│   ├── backup.sh
│   └── hello.sh
├── docker/
│   └── Dockerfile
├── .dockerignore
├── logs/
│   └── network.log
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```
