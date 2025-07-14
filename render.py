import csv

def get_csv_cell(file_path, row_index, column_index=0):
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile))

        if row_index >= len(reader):
            raise IndexError(f"Row {row_index} does not exist in the file.")

        row = reader[row_index]

        if column_index >= len(row):
            raise IndexError(f"Column {column_index} does not exist in row {row_index}.")

        return str(row[column_index])


def count_occupied_rows(file_path):
    count = 0
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Count row only if it has at least one non-empty cell
            if any(cell.strip() for cell in row):
                count += 1
    return int(count)



from fpdf import FPDF
import os

def to_latin1(text: str) -> str:
    # Replace unsupported chars with '?' (or drop them: use 'ignore' instead of 'replace')
    return text.encode('latin-1', 'replace').decode('latin-1')

def save_all_to_pdf(pages_text_list, output_path="pdf_outputs/parsed_results.pdf"):
    # ensure directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)  # built‑in, Latin‑1 only

    for i, page_text in enumerate(pages_text_list):
        pdf.add_page()
        latin_text = to_latin1(page_text)
        for line in latin_text.splitlines():
            pdf.multi_cell(0, 10, line)
        if i != len(pages_text_list) - 1:
            pdf.ln(10)  # blank space between pages

    pdf.output(output_path)
    print(f"[INFO] PDF saved to: {output_path}")
save_all_to_pdf(["Sample text for page 1", "Sample text for page 2"])