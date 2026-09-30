# locales — per-language overlays

Each folder here holds the **differences** that turn the canonical
profile into a language edition. The canonical files at the repo root
are the single source of truth; editions are built, never hand-edited.
The only place a translation is ever edited is its overlay file.

## Rules

- **Mirror the repo path.** `locales/tl/README.md` replaces the root
  `README.md`. `locales/tl/essentials/00-introduction/lessons/christian.md`
  replaces that lesson.
- **UTF-8, no BOM.** Canonical lesson files are cp1252 (legacy); every
  overlay file is UTF-8 so Tagalog, Vietnamese, Thai, Korean and
  Japanese all encode cleanly.
- **Translate what the young person reads.** README, lessons, onboarding
  wording, ritual text. Keep the machinery English: `skills/`,
  `profile.yaml`, plugins, code. The agent already speaks the student's
  language at runtime (the `language` memory key); the overlay makes the
  product feel native on disk.
- **Terms are locked** to the published guide edition for that language
  (tl: kabataan, mag-aaral, Ang Walong Mahalaga). The audience word is
  never the local "teen" word. No em dashes in prose; code blocks and
  commands stay English in every translation.

## Building an edition

    python build_locale.py tl

Produces `dist/onetoeight-agent-tl.zip`, containing a top-level
`onetoeight-agent/` folder. The folder keeps the canonical name so the
profile machinery, plugin keys and docs stay identical across editions.
Ship the zip; never ship the repo.

## Status

**All nine editions complete (30 September 2026): tl, ms, th, vi, id,
es, zh, ko, ja** — each with README + essentials/00-introduction lessons
(christian + universal), QA-swept clean, built and verified.

- **tl (Filipino)** — sample edition and pipeline proof.
- **id (Bahasa Indonesia)** — polished from the reviewed README draft.
- **ms, th, vi, es, zh, ko, ja** — translated against each published
  guide edition (terminology and register locked to it).

Further lessons translate chapter by chapter in later passes; anything
not yet overlaid stays English inside the edition.

## Adding a language

1. Create `locales/<lang>/` and place each file to translate, keeping
   the repo path.
2. Translate against the published guide edition
   (`https://www.onetoeight.guide/<lang>/u/`) so terminology matches
   the shipped work.
3. Run the translation QA sweep (afterschool-agent skill,
   `scripts/qa_translated_markdown.py`): em-dash, banned audience
   words, code-fence parity.
4. `python build_locale.py <lang>` and inspect `dist/`.
