# Reverse Waterfall — Validation Record

Status: **golden / redesigned / production Full verified / Kindle verified**

Updated: 2026-08-29

## Artifact

Repository path:

```text
reverse-waterfall/reverse-waterfall-demo.epub
```

Immutable verified golden URL:

```text
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/7353024813a9dda752772e33903330ab18f6a5e2/reverse-waterfall/reverse-waterfall-demo.epub
```

This exact immutable commit is the promoted Store/regression golden.

Verified artifact:

```text
immutable commit: 7353024813a9dda752772e33903330ab18f6a5e2
EPUB blob: c284347713dba8a3cf828e724fb088c6d55e6e5d
EPUB size: 82,505 bytes
cover blob: f077fe300bdfc45501cffae49c946ec17c8ec821
cover format: JPEG / 1600×2560 / 3-component / 8-bit sRGB
build workflow: 33241537373 / success
exact-byte Kindle smoke: 33241687082 / success
conversion exit code: 0
```

## Exact-byte standards validation — production Full profile

EPUB Preflight Apify Actor:

```text
epubpreflight/epub-preflight
```

The production Full-profile result below is for the exact immutable redesigned EPUB URL recorded above.

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

epub-preflight 0.6.1 | completed | ok=true
epubcheck      5.3.0 | completed | ok=true
ace            1.4.6 | completed | ok=true

errors: 0
warnings: 0
root_causes: 0
actionable_issues: 0

Actor run: gIggUkF2cIiTDAMYk
GitHub hosted smoke: 33242025956
```

## Notes

Earlier fixture iterations intentionally went through the same hosted stack and exposed two useful compatibility details:

- EPUBCheck 5.3.0 warns when the reserved `schema` prefix is explicitly redeclared.
- DAISY Ace expects a matching ARIA role for the `epub:type="toc"` navigation element.

The final fixture removes the redundant reserved-prefix declaration and adds `role="doc-toc"`.

The packaged cover is now a flattened 1600×2560 RGB JPEG. The editable vector artwork remains at `assets/cover-source.svg`, but SVG is not included as the EPUB cover image. The repository build workflow performs this normalization deterministically.

## Maintenance rule

Do not overwrite the meaning of this verification record by changing the immutable URL.

If the fixture or validator stack changes, validate the new bytes independently. Promote a new immutable commit URL only after the intended standards and retailer-specific checks for that release candidate are complete.


## Kindle-conservative compatibility revision

Earlier iterations moved away from an SVG packaged cover and then exposed a second practical issue: a structurally valid PNG cover could still fail a local Kindle Previewer conversion path. The final packaged cover is therefore normalized to RGB JPEG. The surrounding conservative Kindle ingestion changes are:

- added `toc.ncx` and wired it through `spine toc="ncx"`;
- added the navigation document to the spine so a visible HTML table of contents is available near the beginning;
- retained EPUB 3 `properties="cover-image"`;
- added legacy `<meta name="cover" content="cover"/>` metadata;
- kept the editable SVG source outside the EPUB and normalized the packaged cover to RGB JPEG.

The promoted redesigned golden is Kindle-verified independently from the hosted validator stack.

Promoted golden exact-byte smoke:

```text
workflow: Kindle Previewer Smoke
run: 33241687082
head: ce9d75947517127ce1304c68fb9979f6bf626bd5
EPUB blob: c284347713dba8a3cf828e724fb088c6d55e6e5d
conclusion: success
conversion exit code: 0
```

The workflow converted the checked-in redesigned EPUB successfully and generated Kindle conversion/quality output. A local JPEG-normalized reproduction also returned `Supported / Success` and produced a KPF artifact.

The exact artifact is now verified on both layers: production Full-profile validation and Kindle Previewer conversion. A second hosted run through the reference agent client (`nF2zfRruW6Ir3pbX2`) independently returned `ready`, `publishable=true`, and `continue_release`.
