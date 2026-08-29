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

Production smoke run: `ZxQAqBZlYGsYOBkYD`

See [reverse-waterfall/VALIDATION.md](reverse-waterfall/VALIDATION.md) for the frozen verification record.

## Download

### Immutable verified URL

Use this URL in automated examples and golden tests:

```text
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/adc5a6b94e3b48e93dec243824dc1f44e085e836/reverse-waterfall/reverse-waterfall-demo.epub
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
│     ├─ build-reverse-waterfall.yml
│     └─ kindle-previewer-smoke.yml
├─ README.md
├─ LICENSE-NOTICE.md
└─ reverse-waterfall/
   ├─ VALIDATION.md
   ├─ assets/
   │  └─ cover-source.svg
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
         ├─ cover.png
         ├─ nav.xhtml
         ├─ toc.ncx
         ├─ titlepage.xhtml
         ├─ poem.xhtml
         ├─ about.xhtml
         └─ style.css
```

## Kindle compatibility notes

The canonical fixture uses a PNG cover inside the EPUB, retains a separate editable SVG cover source outside the packaged EPUB, includes both EPUB 3 `nav.xhtml` navigation and a compatibility NCX, and declares both the EPUB 3 `cover-image` property and legacy cover metadata. These additions are intentionally conservative for Kindle conversion compatibility while remaining clean under EPUBCheck and DAISY Ace.

Kindle Previewer is a separate retailer-specific conversion layer, so its evidence is tracked independently from standards validation.

The current golden EPUB also passes the Windows GitHub Actions Kindle Previewer smoke workflow. Run `33239124405` installed Kindle Previewer 3.106.0 on `windows-latest`, converted the EPUB with exit code 0, and uploaded the generated Kindle conversion/quality artifacts. The same EPUB also returned `Book converted successfully!` through the Kindle Previewer CLI on a local Windows machine. A GUI-only conversion failure observed on that machine is therefore treated as a local Previewer environment/UI issue rather than an EPUB compatibility failure.

## Rebuilding the fixture

Run:

```bash
python reverse-waterfall/build_epub.py
```

The build workflow rasterizes the editable SVG cover source to a 1600×2560 PNG for broad retailer compatibility. The Python build script then creates the EPUB with a fixed ZIP timestamp, writes the required `mimetype` entry first and uncompressed, and packages the remaining EPUB resources deterministically.

The GitHub Actions workflow rebuilds the binary whenever the EPUB source or builder changes and commits the resulting fixture if its bytes changed.

## Rights and licensing

The repository is public so validation tools and agents can download the fixtures directly.

The poem **Reverse Waterfall** is not open-source content. Copyright remains with Yakshawan. See [LICENSE-NOTICE.md](LICENSE-NOTICE.md) for the permitted testing and demonstration use.

If a future validator version changes the clean result, create a new verified fixture revision rather than silently changing the immutable golden URL.
