import csv
import os
import math
import sys

def split_csv_into_4(input_csv_path):
    # Get base name and extension
    base_name, ext = os.path.splitext(input_csv_path)

    with open(input_csv_path, newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f))

    if not reader:
        raise ValueError("CSV file is empty")

    header = reader[0]
    rows = reader[1:]

    total_rows = len(rows)
    chunk_size = math.ceil(total_rows / 4)

    parts = [
        rows[0:chunk_size],
        rows[chunk_size:chunk_size * 2],
        rows[chunk_size * 2:chunk_size * 3],
        rows[chunk_size * 3:]
    ]

    for i, part in enumerate(parts, start=1):
        output_path = f"{base_name}_part{i}{ext}"
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(part)

        print(f"Written: {output_path} ({len(part)} rows)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split_csv.py <input_csv_file>")
        sys.exit(1)

    split_csv_into_4(sys.argv[1])
