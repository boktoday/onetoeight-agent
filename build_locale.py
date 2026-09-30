# -*- coding: utf-8 -*-
"""Build a language edition of the OneToEight Agent profile.

Usage:
    python build_locale.py tl

Composes the canonical profile (this repo's root, minus dev folders)
with the overlay in locales/<lang>/, then writes
dist/onetoeight-agent-<lang>.zip containing a top-level
onetoeight-agent/ folder (the folder keeps the canonical name so the
profile machinery, plugin keys and docs stay identical across editions).
"""
import datetime
import os
import pathlib
import re
import shutil
import subprocess
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
LOCALES = ROOT / "locales"
DIST = ROOT / "dist"

SKIP_DIRS = {".git", "dist", "locales", "__pycache__", ".venv", "venv"}
SKIP_FILES = {".DS_Store", "Thumbs.db", "build_locale.py"}
SKIP_SUFFIX = (".pyc",)
SKIP_README_SIBLING = re.compile(r"^README\.[a-z]{2}\.md$")

LANG_NAMES = {
    "tl": "Filipino (Tagalog)", "id": "Bahasa Indonesia", "ms": "Bahasa Melayu",
    "vi": "Tiếng Việt", "th": "ไทย", "es": "Español", "zh": "中文",
    "ko": "한국어", "ja": "日本語",
}


def build(lang):
    overlay = LOCALES / lang
    if not overlay.is_dir():
        avail = ", ".join(sorted(p.name for p in LOCALES.iterdir() if p.is_dir())) or "(none)"
        print("No overlay for '%s'. Available: %s" % (lang, avail))
        return 2

    out = DIST / ("onetoeight-agent-" + lang)
    shutil.rmtree(out, ignore_errors=True)
    out.mkdir(parents=True)

    # 1) canonical tree
    n_canon = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [x for x in dirnames if x not in SKIP_DIRS]
        rel_dir = pathlib.Path(dirpath).relative_to(ROOT)
        for fn in filenames:
            if fn in SKIP_FILES or fn.endswith(SKIP_SUFFIX) or SKIP_README_SIBLING.match(fn):
                continue
            dst = out / rel_dir / fn
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(pathlib.Path(dirpath) / fn, dst)
            n_canon += 1

    # 2) overlay on top
    replaced, added = [], []
    for dirpath, dirnames, filenames in os.walk(overlay):
        for fn in filenames:
            src = pathlib.Path(dirpath) / fn
            rel = src.relative_to(overlay)
            dst = out / rel
            (replaced if dst.exists() else added).append(rel.as_posix())
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    # 3) stamp
    try:
        commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                                cwd=str(ROOT), capture_output=True, text=True,
                                timeout=20).stdout.strip() or "unknown"
    except Exception:
        commit = "unknown"
    stamp = ("# OneToEight Agent -- %s edition\n\n"
             "- Locale: %s\n- Overlay files applied: %d\n"
             "- Built from canonical commit: %s\n- Built on: %s\n"
             "- Guide edition for this language: https://www.onetoeight.guide/%s/u/\n") % (
        LANG_NAMES.get(lang, lang), lang, len(replaced) + len(added), commit,
        datetime.date.today().isoformat(), lang)
    (out / "LOCALE.md").write_text(stamp, encoding="utf-8", newline="\n")

    # 4) zip
    zip_path = DIST / ("onetoeight-agent-%s.zip" % lang)
    if zip_path.exists():
        zip_path.unlink()
    n_zip = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(out.rglob("*")):
            if p.is_file():
                z.write(p, arcname="onetoeight-agent/" + p.relative_to(out).as_posix())
                n_zip += 1

    # 5) verify
    checks = [
        ("no locales/ or .git/ in build",
         not (out / "locales").exists() and not (out / ".git").exists()),
        ("README.md overlaid (differs from canonical)",
         (out / "README.md").read_bytes() != (ROOT / "README.md").read_bytes()),
        ("intro lesson overlaid (differs from canonical)",
         (out / "essentials/00-introduction/lessons/christian.md").read_bytes()
         != (ROOT / "essentials/00-introduction/lessons/christian.md").read_bytes()),
        ("machinery intact (SOUL.md, skills/, profile.yaml)",
         (out / "SOUL.md").exists() and (out / "skills").is_dir() and (out / "profile.yaml").exists()),
        ("LOCALE.md present", (out / "LOCALE.md").exists()),
    ]
    ok = all(c[1] for c in checks)
    print("built: %s" % zip_path)
    print("  canonical files: %d | overlay replaced: %d | overlay new: %d | zip entries: %d | size: %.1f MB"
          % (n_canon, len(replaced), len(added), n_zip, zip_path.stat().st_size / 1048576.0))
    for name, passed in checks:
        print("  [%s] %s" % ("ok" if passed else "FAIL", name))
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(build(sys.argv[1]))
