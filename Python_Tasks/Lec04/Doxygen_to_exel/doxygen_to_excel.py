from bs4 import BeautifulSoup
import openpyxl
import csv

# open the html file that contain the doxygen documentaiton

# Path to your local HTML file
file_path = "/home/abdalla-hany/Videos/Embedded Linux Diploma/00.Embedded Linux Tasks/Python_Tasks/Lec04/Doxygen_to_exel/project_documentation/html/functions_8cpp.html"

# Read the content of the HTML file
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "lxml")

functions_names = []
fucntions_discriptions = []
functions_inputs = []
functions_returns = []

# Extracting all functions names
function_name = soup.find_all("h2", {"class": "memtitle"})
for name in list(function_name):
    functions_names.append(name.contents[1].text.strip("()"))

# Extracting all functions discriptions
function_dis = soup.find_all("div", {"class": "memdoc"})
for name in list(function_dis):
    fucntions_discriptions.append(name.contents[1].text.strip(".  "))

# Extracting all functions return data
function_return = soup.find_all("dl", {"class": "section return"})
for name in list(function_return):
    functions_returns.append(name.contents[1].text)

# Extracting all functions inputs
function_ins = soup.find_all("div", {"class": "memdoc"})
for name in list(function_ins):
    a = name.find_all("td", {"class": "paramname"})
    for b in a:
        b = str(b).removeprefix('<td class="paramname">').removesuffix("</td>")
        functions_inputs.append(b)

csv_table = {
    "Functions Names": functions_names,
    "Functions Inputs": functions_inputs,
    "Functions Returns": functions_returns,
    "Functions Descriptions": fucntions_discriptions,
}


# Get the headers (keys of the dictionary)
headers = csv_table.keys()

# Open the CSV file for writing
with open('Functions Documentation.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the headers
    writer.writerow(headers)
    
    # Write the rows
    for row in zip(*csv_table.values()):
        writer.writerow(row)

print("CSV file has been created.")