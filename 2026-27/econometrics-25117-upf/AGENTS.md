# Econometrics 25117 Course Instructions

These instructions apply to files under this course folder.

## Lecture Slide Format

- Current lecture sources live in the course root as `LectureNv2.tex`, with no spaces in the file name, for example `Lecture1v2.tex` and `Lecture10v2.tex`.
- Superseded current-year lecture sources live in `old/` with their original names, for example `old/Lecture 1.tex`.
- Superseded lecture PDFs belong in `old/` alongside the corresponding old lecture sources, for example `old/Lecture1.pdf`.
- Prior-year archive material lives in `older years/`; do not mix current-year superseded files into that folder.
- Preserve the Beamer style already used by `Lecture1v2.tex`: same document class, theme setup, colors, margins, footer, author, institute, and title styling.
- Use the title pattern `\title[]{\textcolor{blue}{Lecture N v2:\\Lecture Title}}` for active current-year lecture sources.
- When creating a v2 lecture from an older `Lecture N.tex`, copy the lecture-specific content, update only the versioned title unless the user asks for content changes, and move the unversioned source into `old/`.
- Keep active lecture sources in the course root so relative paths such as `images/...` continue to work.

## Course-Wide Frames

- If a lecture includes course policy or outline frames, keep them consistent with `Lecture1v2.tex`: participation 5%, Midterm 1 15%, Midterm 2 20%, and cumulative final exam 60%.
- Use the three-block course outline from `Lecture1v2.tex` when an outline frame is needed.

## Editing Discipline

- Do not reformat lecture bodies opportunistically.
- Do not move PDFs, images, exams, practice materials, or prior-year archives unless the user asks for those specific files.
- Compile or otherwise verify only the files touched, and run compilation from the course root.

## Artifact Hygiene

- Keep course authoring and final teaching artifacts as `.tex` and `.pdf` files wherever practical.
- Treat LaTeX build products such as `.aux`, `.log`, `.nav`, `.snm`, `.out`, `.toc`, `.fls`, `.fdb_latexmk`, `.bcf`, `.run.xml`, and `.synctex.gz` as disposable. Compile into a temporary directory when possible, and remove these files after compilation.
- Remove stale `tmp/` build folders and `.DS_Store` files from the course project; do not commit them.
- Keep required source dependencies such as `images/` and bibliography files. The `.tex` and `.pdf` rule applies to authored and delivered course documents, not to assets required to compile them.
- Keep the active syllabus source and its PDF together in `syllabus/`.
