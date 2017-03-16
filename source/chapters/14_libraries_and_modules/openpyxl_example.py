"""
Example using OpenPyXL to create an Excel worksheet
"""

from openpyxl import Workbook
import random

# Create an Excel workbook
wb = Workbook()

# Grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells
ws['A1'] = "This is a test"

# Rows can also be appended
for i in range(200):
    ws.append([random.randrange(1000)])

# Save the file
wb.save("sample.xlsx")
