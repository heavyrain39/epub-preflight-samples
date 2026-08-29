# EPUB Preflight Samples

Public EPUB fixtures for testing and demonstrating [EPUB Preflight](https://apify.com/epubpreflight/epub-preflight).

## Canonical sample

### Reverse Waterfall

`reverse-waterfall/reverse-waterfall-demo.epub` is the canonical public sample for EPUB Preflight. The `main` branch currently carries the redesigned release candidate; the immutable URL below remains the stable baseline until the candidate completes production Full-profile revalidation.

- Title: **Reverse Waterfall**
- Author: **Yakshawan**
- Language: English
- Format: EPUB 3
- Content: poem + title page + sample note
- Build: deterministic Python script
- Intended use: hosted validation, API examples, smoke tests, and documentation

The fixture is intentionally small. The stable baseline has clean hosted-validation evidence, while the redesigned `main` candidate has completed deterministic rebuild and Kindle Previewer smoke and is awaiting an exact-byte production Full-profile rerun.

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

The stable JPEG baseline is additionally verified by Kindle Previewer on Windows:
workflow run `33240892616`, head `299f353070e7454750fd6213ac34331e77e49586`, conversion exit code 0.

The redesigned release candidate was rebuilt by workflow run `33241537373`. The generated cover is a 1600×2560, 3-component, 8-bit sRGB JPEG and the rebuilt EPUB is 82,505 bytes. The exact rebuilt EPUB bytes were then verified by Kindle Previewer in run `33241687082` at head `ce9d75947517127ce1304c68fb9979f6bf626bd5`, conversion exit code 0. Its EPUB blob is `c284347713dba8a3cf828e724fb088c6d55e6e5d`.

Production Full-profile validation for these redesigned bytes is intentionally deferred to the finalization audit.

See [reverse-waterfall/VALIDATION.md](reverse-waterfall/VALIDATION.md) for the
separated standards and retailer-specific evidence.

## Download

### Immutable stable baseline URL

Use this URL in automated examples and golden tests:

```text
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/299f353070e7454750fd6213ac34331e77e49586/reverse-waterfall/reverse-waterfall-demo.epub
```

### Latest main-branch build

```text
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/main/reverse-waterfall/reverse-waterfall-demo.epub
```

The immutable baseline URL remains preferred for Store examples and regression tests until the redesigned candidate receives exact-byte production Full-profile validation. The finalization audit should then promote the validated candidate commit and update downstream Store/sample references together.

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

The stable baseline passes Kindle Previewer smoke at run `33240892616`. The redesigned candidate's exact rebuilt EPUB bytes pass Kindle Previewer smoke at run `33241687082` (head `ce9d75947517127ce1304c68fb9979f6bf626bd5`, exit code 0). A separately normalized local JPEG reproduction also opened successfully in Kindle Previewer and produced KPF output.

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
