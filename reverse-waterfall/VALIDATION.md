# Reverse Waterfall — Validation Record

Status: **golden / JPEG normalized / Kindle verified**

Updated: 2026-08-29

## Artifact

Repository path:

```text
reverse-waterfall/reverse-waterfall-demo.epub
```

Immutable verified URL:

```text
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/299f353070e7454750fd6213ac34331e77e49586/reverse-waterfall/reverse-waterfall-demo.epub
```

The artifact at that commit was produced by the repository build workflow from the checked-in EPUB source tree.

## Standards baseline — production Full profile

EPUB Preflight Apify Actor:

```text
epubpreflight/epub-preflight
```

This result belongs to the preceding structurally equivalent revision before the final PNG-to-JPEG cover normalization. It is retained as the production standards baseline rather than being misrepresented as an exact-byte result for the current JPEG artifact.

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

The packaged cover is now a flattened 1600×2560 RGB JPEG. The editable vector artwork remains at `assets/cover-source.svg`, but SVG is not included as the EPUB cover image. The repository build workflow performs this normalization deterministically.

## Maintenance rule

Do not overwrite the meaning of this verification record by changing the immutable URL.

If the fixture or validator stack changes, validate the new bytes independently and record a new immutable commit URL.


## Kindle-conservative compatibility revision

Earlier iterations moved away from an SVG packaged cover and then exposed a second practical issue: a structurally valid PNG cover could still fail a local Kindle Previewer conversion path. The final packaged cover is therefore normalized to RGB JPEG. The surrounding conservative Kindle ingestion changes are:

- added `toc.ncx` and wired it through `spine toc="ncx"`;
- added the navigation document to the spine so a visible HTML table of contents is available near the beginning;
- retained EPUB 3 `properties="cover-image"`;
- added legacy `<meta name="cover" content="cover"/>` metadata;
- kept the editable SVG source outside the EPUB and normalized the packaged cover to RGB JPEG.

The exact current JPEG golden is Kindle-verified independently from the hosted validator stack.

GitHub Actions Windows smoke:

```text
workflow: Kindle Previewer Smoke
run: 33240892616
head: 299f353070e7454750fd6213ac34331e77e49586
conclusion: success
conversion exit code: 0
```

The workflow converted the checked-in EPUB successfully and generated Kindle conversion/quality output. A local JPEG-normalized reproduction also returned `Supported / Success` and produced a KPF artifact.

A production Full-profile rerun should be recorded after the v0.6.1 Actor is deployed; until then, the earlier production 0-error / 0-warning result above remains explicitly historical evidence, not an exact-byte claim for this JPEG revision.
