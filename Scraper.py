############################################################################################################
# Before Running the program, make an empty file and name it as "database.txt"
# Enter the seach query in the variable string
# After running the script, the latitude and longitudes will be saved in the database file.
############################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

string = raw_input("Enter Search Query: ")
driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.google.co.in")
user_field = driver.find_element_by_css_selector('input[type=text]')
user_field.send_keys(string + "\n")
time.sleep(4)
maps = driver.find_element_by_id('lu_map').click()
time.sleep(4)
dat = driver.page_source

dat = dat.encode('utf-8')
f = open("sample.txt", "w")
f.write(str(dat))
f.flush()
f.close()

f = open("sample.txt", "r")
data = f.read()

lat=[]
lng=[]
k=0
while(k!=-1):
	a = data.find('data-lat', k)
	b = data.find("\"", a+10)
	lat.append(data[a+10:b])
	c = data.find("\"", b+12)
	lng.append(data[b+12:c])
	k=data.find('data-lat', a+10)

s = open("database.txt", "a")
for i in range(len(lat)):
	s.write("lat: " + lat[i] + " | " + "lng: " + lng[i] + "\n")
s.close()


