from openpyxl import Workbook

excel_movies = Workbook()
ws1 = excel_movies.active
ws2 = excel_movies.create_sheet("Sheet_2")

my_file = open('Demograpfic.txt', 'r')
column_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
row_number = 0
column_number = 0
for line in my_file:
    elements = line.split(",")
    for element in elements:
        key = column_letters[column_number]+str(row_number + 1)
        ws1[key] = element
        column_number += 1
    row_number += 1
    column_number = 0
excel_movies.save("DemographicData.xlsx")
