# Book builds

The book is generated from the same Markdown sources as the web course.

Planned release artifacts:

- C64-Codecraft-NO.pdf
- C64-Codecraft-NO.epub
- C64-Codecraft-EN.pdf
- C64-Codecraft-EN.epub

Generated books are release artifacts, not source-of-truth documents.

## Build

Run `make book` with Pandoc and XeLaTeX available. The build reads the ordered canonical lesson sources directly from `course/no` and `course/en`; no book-specific lesson copies are maintained.

CI produces the four files as a build artifact. A release workflow may later attach the same qualified outputs to tagged releases.
