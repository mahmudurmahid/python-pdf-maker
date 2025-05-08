# 📄 Python PDF Maker

The **Python PDF Maker** is a utility script that generates structured PDF documents from a CSV file containing topics and the number of pages per topic. Each topic starts on a new page with a custom header and footer, and every page includes evenly spaced horizontal lines, ideal for creating printable note-taking templates.

This tool is useful for teachers, students, and professionals who want to create structured notebook-style PDFs with labeled headers and consistent page formatting.

---

## 📑 CONTENTS

- [User Experience](#user-experience-ux)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Page Structure](#page-structure)
  - [Color Scheme & Typography](#color-scheme--typography)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Planned Improvements](#planned-improvements)
- [Technologies Used](#technologies-used)
  - [Languages](#languages-used)
  - [Libraries](#libraries-used)
- [Project Files](#project-files)
- [Installation & Usage](#installation--usage)
  - [How to Run](#how-to-run)
  - [Modifying the Input File](#modifying-the-input-file)
- [Testing](#testing)
- [Credits](#credits)

---

## 🧠 User Experience (UX)

### User Stories

As a user, I want to:

- Convert structured CSV data into a custom-formatted multi-page PDF.
- Automatically generate multiple pages per topic without repetitive manual setup.
- Have consistent headers and footers across all pages for professional output.
- Customize topics and page counts quickly using a simple CSV file.

---

## 🎨 Design

### Page Structure

Each PDF page includes the following:

- **Header:** The topic name in large bold text at the top left of the first page of each topic.
- **Lines:** Horizontal lines spaced every 10mm for writing space (from 20mm to 297mm).
- **Footer:** A topic label at the bottom right of every page (italicized and grayed out).

### Color Scheme & Typography

- **Font Family:** Times (classic serif font)
- **Header Font Style:** Bold, size 24, color RGB (100, 100, 100)
- **Footer Font Style:** Italic, size 10, color RGB (180, 180, 180)
- **Background:** White with gray line accents (for easy printing and writing)

---

## 🛠 Features

### Implemented Features

- ✅ Reads topics and page counts from `topics.csv`.
- ✅ Automatically adds a new page for each topic.
- ✅ Draws horizontal lines on each page (like ruled paper).
- ✅ Includes topic headers on first page and footers on all pages.
- ✅ Uses modular iteration logic for easy updates.

### Planned Improvements

- 🔄 Add the option to include a cover page or table of contents.
- 🔄 Enable dynamic line spacing and margins via a config file.
- 🔄 Allow different fonts or themes for specific users (students, teachers).
- 🔄 Add page numbers.
- 🔄 Create CLI arguments for dynamic PDF naming and topic filtering.

---

## 💻 Technologies Used

### Languages Used

- Python 3.13

### Libraries Used

| Library                                    | Purpose                            |
| ------------------------------------------ | ---------------------------------- |
| `fpdf`                                     | PDF creation and formatting        |
| `pandas`                                   | Reading and parsing CSV data       |
| `numpy`                                    | (Indirect via pandas)              |
| `python-dateutil`, `pytz`, `six`, `tzdata` | Dependencies required for `pandas` |

---

## 📁 Project Files

```bash
.
├── main.py              # Main script that creates the PDF
├── topics.csv           # Input file with topics and number of pages
├── requirements.txt     # Python dependencies
└── output.pdf           # (Generated) Final PDF file with all content
```
