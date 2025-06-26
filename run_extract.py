from src.preprocessing import extract_all_pdfs

# Jalankan fungsi ekstraksi
extract_all_pdfs("data/raw_reports", "data/processed_txt")

print("Proses ekstraksi selesai.")