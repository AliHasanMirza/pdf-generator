from fpdf import FPDF

def generate_pdf(name: str, email: str, message: str, output_path: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="User Submitted Info", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt=f"Message:\n{message}")
    
    pdf.output(output_path)
