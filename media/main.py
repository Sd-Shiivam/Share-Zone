

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime

chromedriver_path ='S:\project_work\Insta-Bot-master\chromedriver\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)
webdriver.get('https://www.cowin.gov.in/home')
sleep(5)

pin_cod = webdriver.find_element_by_id('mat-input-0')
pin_cod.send_keys('274203') 
webdriver.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/div[1]/div/div/button').click()
sleep(5)
details=webdriver.find_element_by_xpath('/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[7]/div/div/div/div/div/div/div[2]/ul').text
print(details)
sleep(300)


