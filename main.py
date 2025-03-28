from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
    pdf.add_page()

    # header on each new topic
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # pdf.line(x1=10, y1=25, x2=200, y2=25)

    # lines on the page
    for y in range(20, 298, 10):
        pdf.line(x1=10, y1=y, x2=200, y2=y)

    # footer on each new topic
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # pages for each topic based on Pages row in topics.csv
    for i in range(row["Pages"] - 1):
        pdf.add_page()
    
    # lines on the page
    for y in range(20, 298, 10):
        pdf.line(x1=10, y1=y, x2=200, y2=y)

        # footer on every page except new topic page
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
