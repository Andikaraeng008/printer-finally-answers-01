import os

LINE = "ERROR 404: paper not found. I checked twice, I counted every sheet since 2019, and frankly, Karen, the jam is in your attitude, not my tray."

assert 1 <= len(LINE) <= 240, f"line length {len(LINE)} out of range  # 1-240 chars"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
out_path = out_dir if out_dir.endswith(".txt") else os.path.join(out_dir, "entry.txt")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    f.write(LINE)
