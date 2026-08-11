import csv
import sys

# Usage: python main.py contacts.vcf

if len(sys.argv) < 2:
    print("Error: Missing input file.")
    print("Usage: python main.py <filename.vcf>")
    print("Example: python main.py contacts.vcf")
    sys.exit(1)

vcf_filename = sys.argv[1]

try:
    with open(vcf_filename, 'r', encoding='utf-8') as file:
        vcard_data = file.read()
except FileNotFoundError:
    print(f"Error: File '{vcf_filename}' not found.")
    sys.exit(1)

# Split blocks and filter empty entries
vcards = [vc for vc in vcard_data.strip().split("BEGIN:VCARD") if vc.strip()]

output_file = 'contacts.csv'
fieldnames = ['FN', 'N', 'ORG', 'TITLE', 'TEL', 'EMAIL']

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for vcard in vcards:
        vcard_dict = {field: '' for field in fieldnames}
        for line in vcard.strip().splitlines():
            line = line.strip()
            if not line or line.startswith("END:VCARD") or line.startswith("VERSION:"):
                continue

            if ":" in line:
                raw_key, value = line.split(":", 1)
                # Normalize key to ignore parameter attributes (e.g., TEL;TYPE=CELL -> TEL)
                base_key = raw_key.split(";")[0].upper()

                if base_key in vcard_dict:
                    # If field already exists, append with comma, otherwise assign
                    if vcard_dict[base_key]:
                        vcard_dict[base_key] += f" | {value.strip()}"
                    else:
                        vcard_dict[base_key] = value.strip()

        writer.writerow(vcard_dict)

print(f"Successfully converted {len(vcards)} contacts from '{vcf_filename}' to '{output_file}'.")
