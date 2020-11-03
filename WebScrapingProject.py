from selenium import webdriver
import openpyxl

Path = "C:\chromedriver.exe"
ExcelPath = "D:\\Project.xlsx"
driver = webdriver.Chrome(Path)
driver.get("https://rpa.hybrydoweit.pl")
AriculeTitlesList= ['Tytul']
AreaList= ['Branza']
LinkList= ['Link']

AriculeTitles = driver.find_elements_by_xpath("html/body/section/div/div/div/article/a")

for AriculeTitle in AriculeTitles:
    title = AriculeTitle.get_attribute('title')
    AriculeTitlesList.append(title)


areas = driver.find_elements_by_xpath("html/body/section/div/div/div/article/div/ul")

for area in areas:
       x = area.text
       AreaList.append(x)


links = driver.find_elements_by_xpath("html/body/section/div/div/div/article/a")


for link in links:
       href = link.get_attribute('href')
       LinkList.append(href)
      
    
driver.quit

wb = openpyxl.Workbook()
ws = wb.active


for row in range(len(LinkList)):
       ws.append([AriculeTitlesList[row],AreaList[row],LinkList[row]])


wb.save(ExcelPath)


































