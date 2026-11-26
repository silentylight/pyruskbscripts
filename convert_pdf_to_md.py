from helpers import load_config
import pymupdf4llm

def convert_pdf_to_markdown(pdf_path, md_path):
    markdown = pymupdf4llm.to_markdown(pdf_path)
    with open(md_path, "w", encoding="utf-8") as file:
        file.write(markdown)

def main():
    config = load_config()
    convert_pdf_to_markdown(config["pdfFileName"], config["mdFileName"])

if __name__ == "__main__":
    main()