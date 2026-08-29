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
https://raw.githubusercontent.com/heavyrain39/epub-preflight-samples/adc5a6b94e3b48e93dec243824dc1f44e085e836/reverse-waterfall/reverse-waterfall-demo.epub
```

The artifact at that commit was produced by the repository build workflow from the checked-in EPUB source tree.

## Production verification

EPUB Preflight Apify Actor:

```text
epubpreflight/epub-preflight
```

The current revised artifact was revalidated against the production Full profile after the Kindle-conservative packaging changes.

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

The packaged cover is now a 1600×2560 PNG. The editable vector artwork remains at `assets/cover-source.svg`, but SVG is not included as the EPUB cover image. This avoids Kindle Previewer warnings for an unsupported SVG cover while keeping the source artwork editable.

## Maintenance rule

Do not overwrite the meaning of this verification record by changing the immutable URL.

If the fixture or validator stack changes, validate the new bytes independently and record a new immutable commit URL.


## Kindle-conservative compatibility revision

After a manual Kindle Previewer conversion failure with the otherwise clean PNG-cover fixture, the package was revised conservatively for Kindle ingestion:

- added `toc.ncx` and wired it through `spine toc="ncx"`;
- added the navigation document to the spine so a visible HTML table of contents is available near the beginning;
- retained EPUB 3 `properties="cover-image"`;
- added legacy `<meta name="cover" content="cover"/>` metadata;
- kept the packaged cover as PNG, with the editable SVG source outside the EPUB.

The revised bytes remain clean under the production Full profile:

```text
status: ready
publishable: true
validation_complete: true
errors: 0
warnings: 0
```

Kindle Previewer confirmation is now complete and remains separate from the hosted validator stack.

GitHub Actions Windows smoke:

```text
workflow: Kindle Previewer Smoke
run: 33239124405
head: 254718bb1514836013d666d01cc7eb900ad90a0f
conclusion: success
Kindle Previewer: 3.106.0
conversion exit code: 0
```

The workflow generated Kindle conversion output, conversion logs, and a quality report and uploaded them as the `kindle-previewer-smoke` artifact. The same golden EPUB also returned `Book converted successfully!` from the Kindle Previewer CLI on a local Windows machine. A GUI-only failure observed on that machine is treated as a local Previewer environment/UI issue, not a golden EPUB blocker.
