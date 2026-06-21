#!/usr/bin/env python3
"""publish_wiki.py — OWNER-RUN publish step for the Wiki user manual.

The 8 source-of-truth pages live in the main repo at `docs/wiki/` (`Home.md`,
`_Sidebar.md`, and the 6 pack pages) so the manual is PR-reviewed and
drift-resistant (spec §10.1). This script publishes that mirror to the live
GitHub Wiki: it clones the repo's `.wiki.git`, copies `docs/wiki/*.md` into the
clone, `git add -A`, commits, and pushes (spec §10.3).

OWNER PREREQUISITE (spec §11): the GitHub Wiki must be ENABLED and INITIALIZED
before the first push. In the repo's GitHub UI go to
Settings → Features → Wikis (tick it on), then create ANY first page in the
Wiki tab. Only after that does the `.wiki.git` remote exist and can be cloned.
Running this script against a never-initialized Wiki will fail at the clone
step.

The wiki clone URL is DERIVED from the `origin` remote (`git remote get-url
origin`, swapping a trailing `.git` for `.wiki.git`) so the owner is never
hard-coded. The documented default is:
    https://github.com/ashley-eyekyam/hse-leadership-skills.wiki.git

CLI:
  (default)   clone the .wiki.git, copy docs/wiki/*.md in, commit, push.
  --dry-run   print every step WITHOUT cloning, copying, committing or pushing
              (touches nothing — used by the verifier to confirm the script
              runs and resolves the URL without going near the live Wiki).
  --repo PATH point at the repo root (default: inferred from this file).
  --message M override the commit message.

Stdlib only (subprocess + shutil + pathlib + tempfile + argparse).
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import List, Optional

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parent

# Documented default — the live value is derived from the origin remote at
# runtime (see wiki_url_from_origin) so the owner is never hard-coded.
DEFAULT_WIKI_URL = "https://github.com/ashley-eyekyam/hse-leadership-skills.wiki.git"

DEFAULT_COMMIT_MESSAGE = "docs(wiki): publish docs/wiki mirror to the Wiki"


def wiki_url_from_origin(repo: Path = REPO) -> str:
    """Derive the `.wiki.git` clone URL from the `origin` remote — swap a
    trailing `.git` for `.wiki.git`. Never hard-codes the owner; falls back to
    the documented default if the remote cannot be read (e.g. no git, no
    origin). Mirrors the helper in extract_skill_cards.py."""
    try:
        out = subprocess.run(
            ["git", "-C", str(repo), "remote", "get-url", "origin"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return DEFAULT_WIKI_URL
    if not out:
        return DEFAULT_WIKI_URL
    if out.endswith(".git"):
        return out[: -len(".git")] + ".wiki.git"
    return out + ".wiki.git"


def _wiki_pages(repo: Path) -> List[Path]:
    """The markdown pages under docs/wiki/ (the publish payload), sorted."""
    src = repo / "docs" / "wiki"
    if not src.is_dir():
        return []
    return sorted(src.glob("*.md"))


def _run(cmd: List[str], cwd: Optional[Path] = None) -> None:
    subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=True)


def publish(repo: Path, wiki_url: str, message: str, dry_run: bool) -> int:
    """Clone the wiki, copy docs/wiki/*.md in, commit, push.

    In --dry-run mode every step is printed and NOTHING is executed — no clone,
    no copy, no commit, no push — so the live Wiki is never touched."""
    pages = _wiki_pages(repo)
    src = repo / "docs" / "wiki"

    if not pages:
        print(f"ERROR: no markdown pages found under {src}", file=sys.stderr)
        return 1

    if dry_run:
        print("[dry-run] publish_wiki.py — no clone, copy, commit or push will run")
        print(f"[dry-run] repo:        {repo}")
        print(f"[dry-run] wiki URL:    {wiki_url}")
        print(f"[dry-run] source dir:  {src}")
        print(f"[dry-run] pages ({len(pages)}):")
        for page in pages:
            print(f"[dry-run]   - {page.name}")
        print("[dry-run] would: git clone <wiki URL> <tmp>")
        print(f"[dry-run] would: copy {len(pages)} page(s) into the clone")
        print("[dry-run] would: git add -A")
        print(f"[dry-run] would: git commit -m {message!r}")
        print("[dry-run] would: git push")
        print("[dry-run] done — live Wiki untouched")
        return 0

    tmp = Path(tempfile.mkdtemp(prefix="hse-wiki-"))
    try:
        clone = tmp / "wiki"
        print(f"Cloning {wiki_url} ...")
        _run(["git", "clone", wiki_url, str(clone)])

        print(f"Copying {len(pages)} page(s) from {src} ...")
        for page in pages:
            shutil.copy2(page, clone / page.name)

        _run(["git", "add", "-A"], cwd=clone)

        status = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(clone), check=True, capture_output=True, text=True,
        ).stdout.strip()
        if not status:
            print("No changes to publish — Wiki already up to date.")
            return 0

        _run(["git", "commit", "-m", message], cwd=clone)
        print("Pushing to the Wiki ...")
        _run(["git", "push"], cwd=clone)
        print("Published.")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(
        description="Publish the docs/wiki mirror to the live GitHub Wiki "
                    "(owner-run; see module docstring for prerequisites)."
    )
    p.add_argument(
        "--dry-run", action="store_true",
        help="print every step without cloning, copying, committing or pushing",
    )
    p.add_argument(
        "--repo", default=str(REPO),
        help="repo root (default: inferred from this script's location)",
    )
    p.add_argument(
        "--message", default=DEFAULT_COMMIT_MESSAGE,
        help="commit message for the wiki commit",
    )
    args = p.parse_args(argv)
    repo = Path(args.repo).resolve()
    wiki_url = wiki_url_from_origin(repo)
    return publish(repo, wiki_url, args.message, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
