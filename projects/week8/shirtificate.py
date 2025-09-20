from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", format="A4")
pdf.add_page()
pdf.set_auto_page_break(auto=False)

pdf.set_font("Arial", "B", 24)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 30, "CS50 Shirtificate", align="C", ln=1)

pdf.image("shirtificate.png", x=55, y=60, w=100)

pdf.set_font("Arial", "B", 20)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, 90)
pdf.cell(0, 10, name, align="C")

pdf.output("shirtificate.pdf")
