# teeTimeFinder

# teeTimeFinder

A minimal Python prototype that fetches and prints the HTML for a golf course tee-time “search matrix” page (Quick18) using `requests` and `BeautifulSoup`.

At the moment, this repo is a **single-file spike**: it retrieves one hard-coded URL and prints the parsed HTML to stdout. It is intended as a starting point for building a tee-time monitor / parser (e.g., extract available times, filter by time window, notify when slots open).

---

## What it does (current behavior)

- Sends an HTTP `GET` request to a Quick18 tee-time search URL
- Parses the returned HTML using BeautifulSoup
- Prints the full HTML (prettified) to the console

---

## Project structure

- `main.py` — prototype script (fetch + print HTML)
- `pyproject.toml` / `poetry.lock` — dependency management (Poetry)
- `.replit` / `replit.nix` — Replit configuration (optional)
- `venv/` — included in the zip; **should not be committed** to GitHub

---

## Requirements

- Python 3.10+
- Dependencies:
  - `requests`
  - `bs4` (BeautifulSoup)

---

## Setup

### Option A — Poetry (recommended)

```bash
poetry install
