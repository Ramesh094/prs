import reportlab
from reportlab.pdfgen import canvas

# Create a canvas object
c = canvas.Canvas("report.pdf")

# Draw some text on the canvas
c.drawString(100, 100, "This is a PDF report generated from Excel using Python.")

# Save the canvas object
c.save()