---
name: econometrics-25117-lecture-format
description: Maintain the UPF Econometrics 25117 lecture-slide v2 format and archive convention when editing or creating lecture TeX files in this course folder.
---

# Econometrics 25117 Lecture Format

Use this skill when editing or creating lecture slide sources for `2026-27/econometrics-25117-upf`.

## Active vs Archived Sources

- Active current-year lecture sources should be in the course root as `LectureNv2.tex`, for example `Lecture1v2.tex` and `Lecture10v2.tex`.
- Superseded current-year lecture sources should be in `old/` with their original names, for example `old/Lecture 1.tex`.
- Prior-year archive material belongs in `older years/`, not in `old/`.

## Format To Preserve

Match `Lecture1v2.tex` unless the user explicitly asks for a different style:

- Beamer document class and package/theme setup.
- UPF course metadata: `25117 - Econometrics` and `Universitat Pompeu Fabra`.
- Colors, footer, navigation symbols, margins, and title styling.
- Active title pattern:

```tex
\title[]{\textcolor{blue}{Lecture N v2:\\Lecture Title}}
```

Keep active files in the course root so relative image paths keep resolving.

## Content Rules

- When converting `Lecture N.tex` to `LectureNv2.tex`, preserve lecture-specific content and update only the versioned title unless the user asks for substantive edits.
- If adding or preserving a course-policy frame, use the current evaluation scheme from `Lecture1v2.tex`: participation 5%, Midterm 1 15%, Midterm 2 20%, cumulative final exam 60%.
- If adding or preserving an outline frame, use the three-block course outline from `Lecture1v2.tex`.
- Avoid broad reformatting, unrelated cleanup, or moving non-lecture files.

## Verification

Verify the active lecture paths and titles after edits. If compiling, run from the course root and compile only touched lecture files.
