# Book builds

The book is generated from the same Markdown sources as the web course.

Planned release artifacts:

- C64-Codecraft-NO.pdf\n- C64-Codecraft-NO.epub\n- C64-Codecraft-NO.azw3 (Kindle)\n- C64-Codecraft-EN.pdf\n- C64-Codecraft-EN.epub\n- C64-Codecraft-EN.azw3 (Kindle)

Generated books are release artifacts, not source-of-truth documents.

## Build

Run `make book` with Pandoc, XeLaTeX and Calibre (`ebook-convert`) available. The build reads the ordered canonical lesson sources directly from `course/no` and `course/en`; no book-specific lesson copies are maintained.

CI produces the six files as a build artifact. A release workflow may later attach the same qualified outputs to tagged releases.

## Tagged releases

Tags matching `v*` build the complete NO/EN EPUB, Kindle/AZW3 and PDF set and attach it to the matching GitHub Release together with `SHA256SUMS`. Release publication must only be considered qualified after the workflow has completed successfully for a real tag.

## Localization and covers

Publication metadata is localized in `metadata-no.yaml` and `metadata-en.yaml`. Course Markdown remains format-neutral. Cover artwork will be maintained as publishing assets and must be usable by EPUB, Kindle/AZW3 and PDF without creating format-specific copies of course content.

### Cover filenames

The publication pipeline recognizes `book/cover-no.png` and `book/cover-en.png`. When present, the localized image is embedded as the EPUB cover, propagated into the Kindle/AZW3 conversion, and used as the PDF front page. Builds remain possible without covers so source/toolchain qualification does not depend on artwork being present.
