# How to Add a TFG

This document explains how to add a new TFG (Trabajo Fin de Grado) to the project using the `add_tfg.py` script.

## Prerequisites

- Python 3 installed.
- The project repository cloned and set up.
- A JSON file with the TFG data, based on the `add-tfg-template.json` template.

## Step 1: Prepare the JSON File

Create a JSON file with the following structure, filling in all the required fields:

```json
{
    "title": "Full title of the TFG",
    "resume": "Complete summary of the TFG",
    "author": "Author's full name",
    "tutor": "Tutor's full name",
    "degree": "Academic degree (e.g., Grado En Ingeniería Informática)",
    "year": "Year of defense (e.g., 2025)",
    "month": "Month of defense in lowercase (e.g., septiembre)",
    "pdf_link": "PDF filename (e.g., 2024-25-ETSII-A-XXXX-XXXXXXX-author-MEMORIA.pdf)",
    "github_link": "GitHub repository URL (e.g., https://github.com/user/repo)",
    "keywords": ["keyword1", "keyword2", "keyword3"]
}
```

- **title**: The full title as it should appear.
- **resume**: The complete summary text.
- **author**: Full name of the student.
- **tutor**: Full name of the tutor(s).
- **degree**: The degree program.
- **year**: Four-digit year.
- **month**: Month name in lowercase Spanish (enero, febrero, etc.).
- **pdf_link**: The exact filename of the PDF file that will be placed in the TFG folder or external link in BURJC.
- **github_link**: The URL to the GitHub repository.
- **keywords**: An array of strings for tags (e.g., technologies used).

Use the `add-tfg-template.json` as a starting point.

## Step 2: Run the Script

Execute the script with the JSON file as an argument:

```bash
python add_tfg.py path/to/your_tfg.json
```

Replace `path/to/your_tfg.json` with the actual path to your JSON file.

## What the Script Does

1. **Creates the Folder**: Generates a new folder under `docs/tfgs/YYYY/MM-slug/` where:
   - `YYYY` is the year.
   - `MM` is the two-digit month number (e.g., 09 for septiembre).
   - `slug` is a URL-friendly version of the title (lowercase, spaces to hyphens, special chars removed).

2. **Creates the Individual Page**: Adds an `index.md` file in the new folder with:
   - Title, author, degree, tutor, defense date.
   - Summary.
   - Links to PDF and GitHub.
   - Tags based on keywords.

3. **Updates the Main Index**: Inserts a new card at the top of `docs/index.md` to display the TFG, ensuring the list is sorted by date (newest first).

## Important Notes

- Ensure the JSON is valid and all fields are filled correctly.
- The PDF file should be manually placed in the created folder after running the script.
- If the folder already exists, the script will error out.
- The month must be in lowercase Spanish; it will be capitalized in the output.
- Keywords will appear as tags on both the individual page and the main index.
- After adding, commit and push the changes to update the site.

## Example

Suppose you have `new_tfg.json`:

```json
{
    "title": "My Awesome TFG",
    "resume": "This is a summary...",
    "author": "John Doe",
    "tutor": "Jane Smith",
    "degree": "Grado En Ingeniería Informática",
    "year": "2025",
    "month": "noviembre",
    "pdf_link": "2024-25-ETSII-A-1234-1234567-j.doe-MEMORIA.pdf",
    "github_link": "https://github.com/johndoe/my-tfg",
    "keywords": ["Python", "AI"]
}
```

Run:

```bash
python add_tfg.py new_tfg.json
```

This will create `docs/tfgs/2025/11-my-awesome-tfg/` with the appropriate files and update `docs/index.md`.