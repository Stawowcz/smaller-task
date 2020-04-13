from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import urllib.request as url

class Booking():


    def __init__(self, driver_path, city, room_quantity, adults_quantity):
        
        self.driver_path = driver_path
        self.city = city
        self.room_quantity = room_quantity
        self.adults_quantity = adults_quantity
        self.google_field_name = "q"
        self.google_search_button = "btnK"
        self.booking_search_field = "ss"
        self.calendar_xpath = "//*[@id='frm']/div[1]/div[2]/div/div[2]/div/div/div/div[1]/div/button"
        #self.calendar_xpath = "//*[@id='frm']/div[1]/div[2]/div[1]/div[2]/div/div/div/div/span"
        #self.londyn_first_xpath = "//*[@id='frm']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]"
        #self.calendar_xpath = "//*[@id='frm']/div[1]/div[2]/div/div[2]/div/div/div/div[1]/div/span"
        #self.calendar_xpath = "sb-date-field__icon sb-date-field__icon-btn bk-svg-wrapper calendar-restructure-sb "
        self.room_and_adults_label_id = "xp__guests__toggle"
        self.rooms_id = "no_rooms"
        self.adults_id = "group_adults"
        self.booking_search_button_xpath = "//*[@id='frm']/div[1]/div[4]/div[2]/button"
        self.first_link_xpath = "//*[@id='hotellist_inner']/div[1]/div[2]/div[1]/div[1]/h3/a/span[1]"
        self.driver = webdriver.Chrome(self.driver_path)
    
    def booking_test(self):

        self.driver.set_page_load_timeout(20)
        #1.	wejście na stronę google.pl
        self.driver.get("http://google.com")
        #2.	wpisanie w wyszukiwarce booking
        self.driver.find_element_by_name(self.google_field_name).send_keys('booking')
        #3.	otwarcie linku booking.com
        element = self.driver.find_element_by_name(self.google_search_button)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element_by_partial_link_text('booking.com').click()
        time.sleep(5)
        #4.	wypełnienie pól: dokąd się wybierasz, daty(inna niż dzisiajsza), zmiana liczby pokoi na 2, zmiana liczby dorosłych na 4 
        self.driver.find_element_by_name(self.booking_search_field).send_keys(self.city)
        #time.sleep(1)
        #self.driver.find_element_by_xpath(self.londyn_first_xpath).click()
        #klikniecie w kalendarz
        self.driver.find_element_by_xpath(self.calendar_xpath).click()        
        #wybór pierwszej daty 9 listopada
        self.driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div/div/div[2]/table/tbody/tr[2]/td[5]/span").click()
        #wybór drugiej daty 16 listopada
        self.driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div[2]/div[3]/div/div/div[2]/table/tbody/tr[3]/td[5]/span").click()
        self.driver.find_element_by_id(self.room_and_adults_label_id).click()
        # wybór ilosci pokojów
        select_rooms = Select(self.driver.find_element_by_id(self.rooms_id))
        select_rooms.select_by_value(self.room_quantity)
        # wybór ilosci dorosłych
        select_adults = Select(self.driver.find_element_by_name(self.adults_id))
        select_adults.select_by_value(self.adults_quantity)
        #5.	kliknięcie w szukaj
        self.driver.find_element_by_xpath(self.booking_search_button_xpath).click()
        #6.	kliknięcie w dowolny hotel
        self.driver.find_element_by_xpath(self.first_link_xpath).click()
        time.sleep(3)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        self.driver.save_screenshot("success.png")
        
    def assertion(self):

        #7.	sprawdzenie czy strona się otworzyła
        print ("Current url:\n" +  str(self.driver.current_url))
        assert ("www.booking.com" in self.driver.current_url)
        print("Assertion 1 with 'www.booking.com' passed")
        print ("Website title:\n" + self.driver.title)
        assert ("– aktualne ceny na rok 2018" in self.driver.title)
        print("Assertion 2 with title part '– aktualne ceny na rok 2018' passed")
        
    def check_exit_code(self):

        #7.	sprawdzenie czy strona się otworzyła
        print ("Checking exit code: ")
        print ("Current url:\n" +  str(self.driver.current_url))
        connection = url.urlopen(self.driver.current_url)
        print ("Exit code: " + str(connection.getcode()))
        if (connection.getcode()) == 200:
            print ("Webside succesfully loaded")
        elif (connection.getcode()) == 404:
            print ("Page not found error 404")
        time.sleep(4)
        #self.driver.quit()
        connection.close()
        
        
# Miasto Londyn 2 pokoje 4 dorosłych   
task_selenium = Booking(driver_path = r"d:\userdata\stawowcz\Desktop\drivers\chromedriver.exe", city = "Londyn", room_quantity = '2', adults_quantity = '4')
task_selenium.booking_test()
task_selenium.assertion()
task_selenium.check_exit_code()
#time.sleep(10)
#Miasto: Berlin, 1 pokój, 2 dorosłych
b = Booking(driver_path = r"d:\userdata\stawowcz\Desktop\drivers\chromedriver.exe", city = "Berlin", room_quantity = '1', adults_quantity = '2')
b.booking_test()
b.assertion()
b.check_exit_code()
