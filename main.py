import os

# Kandidat 1, 165 karakter: printer membocorkan isi laporan 47 halaman (rapat bisa jadi email, printer mogok, password masih 'password123') dan menyimpan buktinya.
LINE = "I printed your 47-page report. It says the meeting could have been an email, the printer is on strike, and your password is still 'password123'. I kept the evidence."

assert 1 <= len(LINE) <= 240, f"line length {len(LINE)} out of range  # 1-240 chars"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
out_path = out_dir if out_dir.endswith(".txt") else os.path.join(out_dir, "entry.txt")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    f.write(LINE)
