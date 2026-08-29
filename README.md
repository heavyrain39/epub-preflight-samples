# EPUB Preflight Samples

Public EPUB fixtures for testing and demonstrating [EPUB Preflight](https://apify.com/epubpreflight/epub-preflight).

## Canonical sample

### Reverse Waterfall

`reverse-waterfall/reverse-waterfall-demo.epub` is the canonical public golden sample for EPUB Preflight. The redesigned fixture has completed deterministic rebuild, exact-byte Kindle Previewer smoke, and production Full-profile validation.

- Title: **Reverse Waterfall**
- Author: **Yakshawan**
- Language: English
- Format: EPUB 3
- Content: poem + title page + sample note
- Build: deterministic Python script
- Intended use: hosted validation, API examples, smoke tests, and documentation

The fixture is intentionally small and is now the promoted golden used for Store input, hosted validation, API examples, smoke tests, and regression checks.

### Validation evidence

The redesigned exact-byte artifact passed the production Full profile on 2026-08-29:

```text
Apify Actor run: gIggUkF2cIiTDAMYk
validation_complete = true
status = ready
publishable = true

EPUB Preflight 0.6.1 = completed / ok
EPUBCheck 5.3.0      = completed / ok
DAISY Ace 1.4.6      = completed / ok

errors = 0
warnings = 0
```

The same immutable EPUB was independently consumed through the dependency-free
reference agent client in Actor run `nF2zfRruW6Ir3pbX2`. That second hosted
run also succeeded with `status=ready`, `publishable=true`, zero errors and
warnings, and agent recommendation `continue_release`.

The artifact was rebuilt by workflow run `33241537373`. Its packaged cover is
a 1600×2560, 3-component, 8-bit sRGB JPEG and the EPUB is 82,505 bytes. The
exact rebuilt EPUB bytes passed Kindle Previewer in run `33241687082`
(conversion exit code 0). EPUB blob:
`c284347713dba8a3cf828e724fb088c6d55e6e5d`.

See [reverse-waterfall/VALIDATION.md](reverse-waterfall/VALIDATION.md) for the
separated standards and retailer-specific evidence.

## Download

### Immutable verified golden URL

Use this URL in automated examples and golden tests:

```text
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/7353024813a9dda752772e33903330ab18f6a5e2/reverse-waterfall/reverse-waterfall-demo.epub
```

### Latest main-branch build

```text
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/main/reverse-waterfall/reverse-waterfall-demo.epub
```

The immutable verified URL is the preferred Store, API-example, and regression-test input. Future fixture revisions must receive fresh exact-byte standards and retailer-specific validation before this URL is replaced.

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

The promoted golden's exact rebuilt EPUB bytes pass Kindle Previewer smoke at run `33241687082` (head `ce9d75947517127ce1304c68fb9979f6bf626bd5`, exit code 0). A separately normalized local JPEG reproduction also opened successfully in Kindle Previewer and produced KPF output.

## Rebuilding the fixture

Run:

```bash
python reverse-waterfall/build_epub.py
```

The build workflow rasterizes the editable SVG cover source and normalizes it to a flattened 1600×2560 RGB JPEG for conservative Kindle compatibility. The Python build script then creates the EPUB with a fixed ZIP timestamp, writes the required `mimetype` entry first and uncompressed, and packages the remaining EPUB resources deterministically.

The GitHub Actions build workflow rebuilds the binary whenever the EPUB source or builder changes and commits the resulting fixture if its bytes changed. A successful build now triggers the Kindle Previewer workflow after the rebuild completes, so retailer smoke evidence follows the generated EPUB rather than racing the source commit. Direct EPUB-binary changes still trigger Kindle smoke on push.

## Rights and licensing

The repository is public so validation tools and agents can download the fixtures directly.

The poem **Reverse Waterfall** is not open-source content. Copyright remains with Yakshawan. See [LICENSE-NOTICE.md](LICENSE-NOTICE.md) for the permitted testing and demonstration use.

If a future validator version changes the clean result, create a new verified fixture revision rather than silently changing the immutable golden URL.
