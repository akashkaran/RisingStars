from selenium import webdriver
import time
# create a new Firefox session
driver = webdriver.Firefox()

# navigate to the application  page
driver.get("http://127.0.0.1:8000/predictor/")

#getting data from file
fo = open("sampledata.txt","r")
li=fo.readlines()[1:]
fo.close()
fo=open("results.txt","+w")
for i in li:
		s=i.split()
		#filling data
		driver.find_element_by_name("name").send_keys(s[0]+s[1])
		driver.find_element_by_name("inns").send_keys(s[5])
		driver.find_element_by_name("runs").send_keys(s[7])
		driver.find_element_by_name("avrg").send_keys(s[9])
		driver.find_element_by_name("sr").send_keys(s[11])
		driver.find_element_by_name("hundreds").send_keys(s[12])
		driver.find_element_by_name("fifties").send_keys(s[13])
		driver.find_element_by_name("sixes").send_keys(s[15])
		driver.find_element_by_name("fours").send_keys(s[14])
		driver.find_element_by_name("hs").send_keys(s[8])
		driver.find_element_by_name("bf").send_keys(s[10])
		time.sleep(5)
		driver.find_element_by_css_selector('.btn').click()
		#printing results
		fo.write(k)
		k=driver.find_element_by_id("result").text
		print(k)
