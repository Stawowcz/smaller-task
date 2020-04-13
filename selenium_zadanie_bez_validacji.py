from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(r"d:\userdata\stawowcz\Desktop\drivers\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys('booking')
element = driver.find_element_by_name("btnK")
driver.execute_script("arguments[0].click();", element)
driver.find_element_by_partial_link_text('booking.com').click()
driver.find_element_by_name("ss").send_keys("Londyn")
#klikniecie w kalendarz
driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[2]/div/div[2]/div/div/div/div[1]/div/button").click() 
time.sleep(1)
#wybór 1 daty 9 listopada
driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/span").click()
#klikniecie ptaszka przesuwjacego kaledarz
#driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div[2]/div[2]/span").click()
#klikniecie 2 daty 16 listopada
driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div[2]/div[3]/div/div/div[2]/table/tbody/tr[3]/td[5]/span").click()
driver.find_element_by_id("xp__guests__toggle").click()
select_rooms = Select(driver.find_element_by_id("no_rooms"))
select_rooms.select_by_value('2')
select_adults = Select(driver.find_element_by_name("group_adults"))
select_adults.select_by_value('4')
driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[4]/div[2]/button").click()
driver.find_element_by_xpath("//*[@id='hotellist_inner']/div[1]/div[2]/div[1]/div[1]/h3/a/span[1]").click()
print (driver.current_url)
assert ("google" in driver.title)
time.sleep(4)
driver.quit()
