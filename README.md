# Pyrus Knowledge Base Scripts

Small Python scripts for working with the Pyrus Knowledge Base API: convert a PDF to Markdown, upload a new article, update an existing one, and download an article back to a `.md` file.

## Why

Before writing these scripts, I could spend up to an hour per article moving it between formats and Pyrus: exporting to PDF/HTML, converting to Markdown, working on the text, then transferring everything back and fixing the formatting by hand.
How long it took depended on the size of the manual and how much it changed.
Now each step is a single script, and since Markdown is the working format, editing articles with AI is much easier.

## Scripts

| Script | What it does | Config fields used |
| --- | --- | --- |
| `convert_pdf_to_md.py` | Converts a PDF to Markdown | `pdfFileName`, `mdFileName` |
| `upload_article.py` | Creates a new article from a Markdown file | `login`, `secKey`, `mdFileName`, `titleForArticle`, `topicId` |
| `update_article.py` | Replaces the body of an existing article with a Markdown file | `login`, `secKey`, `mdFileName`, `articleId` |
| `download_article.py` | Saves an article as `<title>.md` in the current folder | `login`, `secKey`, `articleId` |

Shared code (config loading, authentication, error handling, filename sanitizing) lives in `helpers.py`.

## Setup

Install requirements and copy `info.example.json` to `info.json`.
```
pip install -r requirements.txt
```

- Linux/macOS/PowerShell: `cp info.example.json info.json`
- Windows cmd: `copy info.example.json info.json`

Fill in `info.json`. Only the fields used by the script you run need values:

```json
{
    "login": "your-pyrus-login",
    "secKey": "your-security-key",
    "articleId": "ABC123",
    "topicId": "XYZ789",
    "pdfFileName": "input.pdf",
    "mdFileName": "article.md",
    "titleForArticle": "My article"
}
```
`info.json` is listed in `.gitignore`, so your credentials are never committed. All values above are examples.

`mdFileName` means different things depending on the script: for `update_article.py` and `upload_article.py` it is the input file name. For `convert_pdf_to_md.py` it will be used as output file. Keep that in mind.


## Usage

All scripts must be run from the project folder:

```
python convert_pdf_to_md.py
python upload_article.py
python update_article.py
python download_article.py
```

Input files (for example `somedocument.pdf` or `example.md`) must be in that folder too, or use paths relative to it in `info.json`.

## Notes

- Authentication gets a fresh access token on every run, so there is no token to store.
- On an API error, the response body is included in the exception message.
- `update_article.py` changes only the article body.