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

### Validation evidence

The publication structure passed the production Full profile before the final
JPEG cover normalization:

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

Historical production smoke run: `ZxQAqBZlYGsYOBkYD`.

The current JPEG golden is additionally verified by Kindle Previewer on Windows:
workflow run `33240892616`, head `299f353070e7454750fd6213ac34331e77e49586`, conversion exit code 0.

See [reverse-waterfall/VALIDATION.md](reverse-waterfall/VALIDATION.md) for the
separated standards and retailer-specific evidence.

## Download

### Immutable verified URL

Use this URL in automated examples and golden tests:

```text
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/299f353070e7454750fd6213ac34331e77e49586/reverse-waterfall/reverse-waterfall-demo.epub
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
         ├─ cover.jpg
         ├─ nav.xhtml
         ├─ toc.ncx
         ├─ titlepage.xhtml
         ├─ poem.xhtml
         ├─ about.xhtml
         └─ style.css
```

## Kindle compatibility notes

The canonical fixture uses a JPEG cover inside the EPUB, retains a separate editable SVG cover source outside the packaged EPUB, includes both EPUB 3 `nav.xhtml` navigation and a compatibility NCX, and declares both the EPUB 3 `cover-image` property and legacy cover metadata. These additions are intentionally conservative for Kindle conversion compatibility while remaining clean under EPUBCheck and DAISY Ace.

Kindle Previewer is a separate retailer-specific conversion layer, so its evidence is tracked independently from standards validation.

The current JPEG golden passes the Windows GitHub Actions Kindle Previewer smoke workflow. Run `33240892616` checked out exact head `299f353070e7454750fd6213ac34331e77e49586`, converted the checked-in EPUB with exit code 0, and produced Kindle conversion/quality output. A separately normalized local JPEG reproduction also opened successfully in Kindle Previewer and produced KPF output.

## Rebuilding the fixture

Run:

```bash
python reverse-waterfall/build_epub.py
```

The build workflow rasterizes the editable SVG cover source and normalizes it to a flattened 1600×2560 RGB JPEG for conservative Kindle compatibility. The Python build script then creates the EPUB with a fixed ZIP timestamp, writes the required `mimetype` entry first and uncompressed, and packages the remaining EPUB resources deterministically.

The GitHub Actions workflow rebuilds the binary whenever the EPUB source or builder changes and commits the resulting fixture if its bytes changed.

## Rights and licensing

The repository is public so validation tools and agents can download the fixtures directly.

The poem **Reverse Waterfall** is not open-source content. Copyright remains with Yakshawan. See [LICENSE-NOTICE.md](LICENSE-NOTICE.md) for the permitted testing and demonstration use.

If a future validator version changes the clean result, create a new verified fixture revision rather than silently changing the immutable golden URL.
