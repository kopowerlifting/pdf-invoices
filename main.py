from fpdf import FPDF
import pandas as pd
import glob

filepaths = glob.glob("invoices/*xlsx")

invoice_list = []

for file in filepaths:
    df = pd.read_excel(file, sheet_name="Sheet 1")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
