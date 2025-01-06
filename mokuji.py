from bs4 import BeautifulSoup
import urllib.request as req
import openpyxl

#--- parameters ---

url = "http://kenkyuyoroku.blog84.fc2.com/blog-entry-659.html"
path = "./tanizaki.xlsx"

#--- import ---
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

li_list = soup.select_one("#center > div.ently_outline > div > div.ently_text")


data = li_list.get_text(",").split(",")

name_list = []
for text in data:
    name = text.split("…")[0]
    name_list.append(name)

#--- export ---

wb = openpyxl.Workbook()
ws = wb.worksheets[0]

for i in range(len(name_list)-1):
    ws.cell(row=i+1, column=1).value = name_list[i]

wb.save(path)