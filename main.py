from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob("invoices/*xlsx")

invoice_list = []

for file in filepaths:
    df = pd.read_excel(file, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(file).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", size=16, style="")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"pdfs/{filename}.pdf")
