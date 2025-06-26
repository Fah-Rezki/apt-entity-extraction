import os
from pathlib import Path
from pdfminer.high_level import extract_text

def extract_all_pdfs(input_dir, output_dir):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for year_folder in sorted(input_path.iterdir()):
        if year_folder.is_dir():
            for pdf_file in year_folder.glob("*.pdf"):
                try:
                    text = extract_text(pdf_file)
                    out_file = output_path / f"{pdf_file.stem}.txt"
                    with open(out_file, "w", encoding="utf-8") as f:
                        f.write(text)
                    print(f"✅ Extracted: {pdf_file.name}")
                except Exception as e:
                    print(f"❌ Failed: {pdf_file.name} – {e}")

# Example usage:
# extract_all_pdfs("data/raw_reports", "data/processed_txt")
