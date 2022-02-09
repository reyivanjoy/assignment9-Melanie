import json
from fpdf import FPDF

pdf = FPDF("P", "mm", "Letter")
pdf.add_page()

resume = open("Resume.json", "r")
resumeInfo = resume.read()
finalResume = json.loads(resumeInfo)

for input in finalResume:
    pdf.set_font("courier", "BU", 24)
    pdf.cell(195, 19.1, str(input["Personal Information"]),border = True, ln =1, align="C")
    
    pdf.set_font("times", "", 12)
    pdf.cell(195, 8, str(input["Last Name"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["First Name"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Middle Name"]),border = True, ln =1)
    
    pdf.set_font("times", "", 12)
    pdf.cell(195, 8, str(input["Sex"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Address"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Age"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Birthdate"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Birthplace"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Citizenship"]),border = True, ln =1)
    
    pdf.set_font("courier", "BU", 24)
    pdf.cell(195, 19.1, str(input["Contact Info"]),border = True, ln =1, align="C")
    
    pdf.set_font("times", "", 12)
    pdf.cell(195, 8, str(input["Contact Number"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Telephone Number"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Email Address"]),border = True, ln =1)
    
    pdf.set_font("courier", "BU", 24)
    pdf.cell(195, 19.1, str(input["EducationalBg"]),border = True, ln =1, align='C')
    
    pdf.set_font("courier", "BU", 16)
    pdf.cell(195, 8, str(input["School1"]),border = True, ln =1)
    
    pdf.set_font("times", "", 12)
    pdf.cell(195, 8, str(input["Primary School"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Academic Year1"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Achievement1"]),border = True, ln =1)
    
    pdf.set_font("courier", "BU", 16)
    pdf.cell(195, 8, str(input["School2"]),border = True, ln =1)
    
    pdf.set_font("times", "", 12)
    pdf.cell(195, 8, str(input["Secondary School"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Academic Year2"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Achievement2"]),border = True, ln =1)
    
    pdf.set_font("courier", "BU", 16)
    pdf.cell(195, 8, str(input["School3"]),border = True, ln =1)
    
    pdf.set_font("times", "", 12)
    pdf.cell(195, 8, str(input["Tertiary School"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Academic Year3"]),border = True, ln =1)
    pdf.cell(195, 8, str(input["Achievement3"]),border = True, ln =1)
    
pdf.output("REY_IVANJOY.pdf")
