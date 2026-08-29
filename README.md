# EPUB Preflight Samples

Public EPUB fixtures for testing and demonstrating [EPUB Preflight](https://apify.com/epubpreflight/epub-preflight).

## Canonical sample

### Reverse Waterfall

`reverse-waterfall/reverse-waterfall-demo.epub` is the canonical small public sample for EPUB Preflight.

- Title: **Reverse Waterfall**
- Author: **Yakshawan**
- Language: English
- Format: EPUB 3
- Content: text-only poem plus a short sample note
- Intended use: hosted validation, API examples, smoke tests, and documentation

The sample is designed to be small, deterministic, and friendly to automated validation across EPUB Preflight, EPUBCheck, and DAISY Ace.

Direct raw URL:

```text
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/main/reverse-waterfall/reverse-waterfall-demo.epub
```

## Repository layout

```text
epub-preflight-samples/
├─ README.md
├─ LICENSE-NOTICE.md
└─ reverse-waterfall/
   ├─ source/
   │  └─ reverse-waterfall-en.md
   └─ reverse-waterfall-demo.epub
```

## Rights and licensing

The repository is public so validation tools and agents can download the fixtures directly.

The poem **Reverse Waterfall** is not open-source content. Copyright remains with Yakshawan. See [LICENSE-NOTICE.md](LICENSE-NOTICE.md) for the permitted testing and demonstration use.

## Validation target

For the canonical sample, the desired hosted EPUB Preflight result is:

```text
validation_complete = true
status = ready
publishable = true
native = completed / ok
epubcheck = completed / ok
ace = completed / ok
errors = 0
warnings = 0
```

If a future validator version changes that result, the fixture should be reviewed and versioned rather than silently replaced.
