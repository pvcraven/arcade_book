"""
Example using OpenPyXL to create an Excel worksheet
"""

from openpyxl import Workbook
import random

# Create an Excel workbook
work_book = Workbook()

# Grab the active worksheet
work_sheet = work_book.active

# Data can be assigned directly to cells
work_sheet['A1'] = "This is a test"

# Rows can also be appended
for i in range(200):
    work_sheet.append(["Random Number:", random.randrange(1000)])

# Save the file
work_book.save("sample.xlsx")
