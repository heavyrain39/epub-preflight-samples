# Reverse Waterfall — Hosted Validation Record

Status: **golden / clean**

Validated: 2026-08-29

## Artifact

Repository path:

```text
reverse-waterfall/reverse-waterfall-demo.epub
```

Immutable verified URL:

```text
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/87a162fa98d584bdd2493c91d4ab3a9015600a76/reverse-waterfall/reverse-waterfall-demo.epub
```

The artifact at that commit was produced by the repository build workflow from the checked-in EPUB source tree.

## Production verification

EPUB Preflight Apify Actor:

```text
epubpreflight/epub-preflight
```

Production smoke run:

```text
h4s4HebffxWwPj9mo
```

Requested profile:

```json
{
  "applySafeFixes": false,
  "runEpubcheck": true,
  "runAce": true
}
```

Observed result:

```text
status: ready
publishable: true
validation_complete: true

epub-preflight 0.6.0 | completed | ok=true
epubcheck      5.3.0 | completed | ok=true
ace            1.4.6 | completed | ok=true

errors: 0
warnings: 0
root_causes: 0
actionable_issues: 0
```

## Notes

Earlier fixture iterations intentionally went through the same hosted stack and exposed two useful compatibility details:

- EPUBCheck 5.3.0 warns when the reserved `schema` prefix is explicitly redeclared.
- DAISY Ace expects a matching ARIA role for the `epub:type="toc"` navigation element.

The final fixture removes the redundant reserved-prefix declaration and adds `role="doc-toc"`.

A declared SVG cover image is also included so the native EPUB Preflight cover check remains clean.

## Maintenance rule

Do not overwrite the meaning of this verification record by changing the immutable URL.

If the fixture or validator stack changes, validate the new bytes independently and record a new immutable commit URL.
