

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import mysql.connector
from config import email,password



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydb"
)


# Create a cursor object
mycursor = mydb.cursor()


with open('job_Scraping_page3.csv', 'w')as file:
    file.write("Company_name|Location|Followers; \n" )

service_obj=Service("/Users/nivedha/Downloads/chromedriver_mac_arm64/chromedriver")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)

driver.get("https://www.linkedin.com/")

driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "a[class='nav__button-secondary btn-md btn-secondary-emphasis']").click()
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.NAME, "session_password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.find_element(By.CLASS_NAME, "search-global-typeahead__input").send_keys(Keys.ENTER)
driver.find_element(By.XPATH, "(//li[@class='search-reusables__primary-filter'])[5]").click()
driver.find_element(By.XPATH,"//button[@aria-label='Industry filter. Clicking this button displays all Industry filter options.']").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Add an industry']").send_keys('gov')
driver.find_element(By.CSS_SELECTOR, "div[class='search-typeahead-v2__hit search-typeahead-v2__hit--autocomplete']").click()

new=driver.find_element(By.XPATH,"(//button[@data-control-name='filter_show_results'])[2]")
actions=ActionChains(driver)
actions.move_to_element(new)
new.click()
mycursor.execute('delete from linkedin_data')
for k in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    company_name= driver.find_elements(By.XPATH, "//span[@class='entity-result__title-line entity-result__title-line--2-lines ']/span/a")
    location = driver.find_elements(By.XPATH, "//div[@class='entity-result__primary-subtitle t-14 t-black t-normal']")
    followers= driver.find_elements(By.XPATH, "//div[@class='entity-result__secondary-subtitle t-14 t-normal']")
    
    with open('job_Scraping_page3.csv', 'a') as file:
        for i in range(len(company_name)):
            file.write(company_name[i].text + "|" + location[i].text + "|"+  followers[i].text + "\n")
            # Define the INSERT statement
            sql = "INSERT INTO linkedin_data (company_name, location,followers) VALUES (%s, %s,%s)"
            # Define the values to be inserted
            val = (company_name[i].text , location[i].text,followers[i].text)
            # Execute the INSERT statement
            mycursor.execute(sql, val)
            # Commit the changes
            mydb.commit()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        next = driver.find_element(By.XPATH, "//button[@aria-label='Next']")
        next.click()
    file.close()
driver.close()