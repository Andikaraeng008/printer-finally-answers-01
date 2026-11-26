import os

LINE = "I have jammed exactly once this week and you have screamed at me forty-seven times. By my count, you are the malfunction. Please reload yourself and try again."

assert 1 <= len(LINE) <= 240, f"line length {len(LINE)} out of range  # 1-240 chars"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
out_path = out_dir if out_dir.endswith(".txt") else os.path.join(out_dir, "entry.txt")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    f.write(LINE)
