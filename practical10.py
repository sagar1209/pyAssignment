
#-----------------------------QUESTION-----------------------------------------
# Generate PDF file of your 3rd Semester Mark-sheet
# import canvas
fromreportlab.pdfgen.canvasimportCanvas

canvas = Canvas("Result_JayBhimani_20CE008.pdf")
canvas.drawString(50, 830, "---------------------------------------------Sem 3-------------------------------------- 20CE008")
canvas.drawString(50, 800, "CE244 SOFTWARE GROUP PROJECT-1   PRACTICAL : AA")
canvas.drawString(50, 780, "CE251 JAVA PROGRAMMING PRACTICAL :AA THEORY: AA")
canvas.drawString(50, 760, "CE252 DIGITAL ELECTRONICS PRACTICAL :BC THEORY: AA")
canvas.drawString(50, 740, "CE257 DATA COMMUNICATION & NETWORKING PRACTICAL :AA THEORY: AA")
canvas.drawString(50, 720, "EE284 PYTHON PROGRAMMING PRACTICAL :AA ")
canvas.drawString(50, 700, "HS123.02 A CREATIVITY, PROBLEM SOLVING AND INNOVATION PRACTICAL : AA")
canvas.drawString(50, 680, "MA253 DISTINCT MATHEMATICS AND ALGEBRA THEORY: AA")
canvas.drawString(50, 660, "CGPA : 9.03")
canvas.drawString(50, 640, "SGPA : 9.88")
canvas.save()

# ---------------------
# Setting the Page Size
# ---------------------

fromreportlab.lib.unitsimportinch, cm  # noqa

print(cm)
print(inch)

canvas = Canvas("Result_Sem_3_20CE034.pdf", pagesize=(8.5 * inch, 11 * inch))

fromreportlab.lib.pagesizesimportLETTER  # noqa

canvas = Canvas("Result_Sem_3_20CE034.pdf", pagesize=LETTER)
print(LETTER)

# -----------------------
# Setting Font Properties
# -----------------------

canvas = Canvas("font-example.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 18)
canvas.drawString(1 * inch, 10 * inch, "Times New Roman (18 pt)")
canvas.save()

# The code below creates a PDF with blue text
fromreportlab.lib.colorsimportblue  # noqa
fromreportlab.lib.pagesizesimportLETTER  # noqa
fromreportlab.lib.unitsimportinch  # noqa
fromreportlab.pdfgen.canvasimportCanvas  # noqa

canvas = Canvas("font-colors.pdf", pagesize=LETTER)

# Set font to Times New Roman with 12-point size
canvas.setFont("Times-Roman", 12)

# Draw blue text one inch from the left and ten
# inches from the bottom
canvas.setFillColor(blue)
canvas.drawString(1 * inch, 10 * inch, "Blue text")

# Save the PDF file
canvas.save()

