import os

# Kandidat 1, 150 karakter: kontrak hilang, printer menghancurkannya untuk mencetak log error 214 halaman yang menjelaskan penghancuran itu, dan mesin penghancur dipromosikan jadi kepala keamanan.
LINE = "Your contract is gone. I shredded it to print the 214-page error log explaining the shredding, and the shredder has been promoted to head of security."

assert 1 <= len(LINE) <= 240, f"line length {len(LINE)} out of range  # 1-240 chars"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
out_path = out_dir if out_dir.endswith(".txt") else os.path.join(out_dir, "entry.txt")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    f.write(LINE)
