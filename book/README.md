# Book builds

The book is generated from the same Markdown sources as the web course.

Planned release artifacts:

- C64-Codecraft-NO.pdf\n- C64-Codecraft-NO.epub\n- C64-Codecraft-NO.azw3 (Kindle)\n- C64-Codecraft-EN.pdf\n- C64-Codecraft-EN.epub\n- C64-Codecraft-EN.azw3 (Kindle)

Generated books are release artifacts, not source-of-truth documents.

## Build

Run `make book` with Pandoc, XeLaTeX and Calibre (`ebook-convert`) available. The build reads the ordered canonical lesson sources directly from `course/no` and `course/en`; no book-specific lesson copies are maintained.

CI produces the six files as a build artifact. A release workflow may later attach the same qualified outputs to tagged releases.
