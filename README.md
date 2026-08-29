# EPUB Preflight Samples

Public EPUB fixtures for testing and demonstrating [EPUB Preflight](https://apify.com/epubpreflight/epub-preflight).

## Canonical sample

### Reverse Waterfall

`reverse-waterfall/reverse-waterfall-demo.epub` is the canonical public golden sample for EPUB Preflight.

- Title: **Reverse Waterfall**
- Author: **Yakshawan**
- Language: English
- Format: EPUB 3
- Content: poem + title page + sample note
- Build: deterministic Python script
- Intended use: hosted validation, API examples, smoke tests, and documentation

The fixture is intentionally small and is built to pass the complete hosted validation stack cleanly.

### Verified production result

The current golden artifact was verified against the production Apify Actor on 2026-08-29:

```text
validation_complete = true
status = ready
publishable = true

EPUB Preflight 0.6.0 = completed / ok
EPUBCheck 5.3.0      = completed / ok
DAISY Ace 1.4.6      = completed / ok

errors = 0
warnings = 0
```

Production smoke run: `h4s4HebffxWwPj9mo`

See [reverse-waterfall/VALIDATION.md](reverse-waterfall/VALIDATION.md) for the frozen verification record.

## Download

### Immutable verified URL

Use this URL in automated examples and golden tests:

```text
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/87a162fa98d584bdd2493c91d4ab3a9015600a76/reverse-waterfall/reverse-waterfall-demo.epub
```

### Latest main-branch build

```text
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/main/reverse-waterfall/reverse-waterfall-demo.epub
```

The immutable URL is preferred for Store examples and regression tests because future fixture revisions cannot silently change its bytes.

## Repository layout

```text
epub-preflight-samples/
├─ .github/
│  └─ workflows/
│     └─ build-reverse-waterfall.yml
├─ README.md
├─ LICENSE-NOTICE.md
└─ reverse-waterfall/
   ├─ VALIDATION.md
   ├─ build_epub.py
   ├─ reverse-waterfall-demo.epub
   ├─ source/
   │  └─ reverse-waterfall-en.md
   └─ epub-src/
      ├─ mimetype
      ├─ META-INF/
      │  └─ container.xml
      └─ EPUB/
         ├─ package.opf
         ├─ cover.svg
         ├─ nav.xhtml
         ├─ titlepage.xhtml
         ├─ poem.xhtml
         ├─ about.xhtml
         └─ style.css
```

## Rebuilding the fixture

Run:

```bash
python reverse-waterfall/build_epub.py
```

The build script creates the EPUB with a fixed ZIP timestamp, writes the required `mimetype` entry first and uncompressed, and packages the remaining EPUB resources deterministically.

The GitHub Actions workflow rebuilds the binary whenever the EPUB source or builder changes and commits the resulting fixture if its bytes changed.

## Rights and licensing

The repository is public so validation tools and agents can download the fixtures directly.

The poem **Reverse Waterfall** is not open-source content. Copyright remains with Yakshawan. See [LICENSE-NOTICE.md](LICENSE-NOTICE.md) for the permitted testing and demonstration use.

If a future validator version changes the clean result, create a new verified fixture revision rather than silently changing the immutable golden URL.
