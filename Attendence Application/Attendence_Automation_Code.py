from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

# create a new Chrome browser instance
driver = webdriver.Chrome()

# navigate to the website
driver.get("https://info.aec.edu.in/aec/")

# find the user name and password input fields and enter the credentials
user_name = driver.find_element(By.ID, 'txtId2')
user_name.send_keys("USERNAME(ROLLNO)")  #<-------------------------------------------    ENTER YOUR USERNAME

password = driver.find_element(By.ID, 'txtPwd2')
password.send_keys("PASSWORD")           #<-------------------------------------------    ENTER YOUR PASSWORD

# click the login button
login_button = driver.find_element(By.ID, "imgBtn2")
login_button.click()

# wait for the page to load
time.sleep(2)  

# navigate to student attendance page
driver.get("https://info.aec.edu.in/aec/Academics/StudentAttendance.aspx?scrid=3&showtype=SA")

# select "Till now" option from the drop-down
till_now_option = driver.find_element(By.ID,"radTillNow")
till_now_option.click()


# click the "Show" button to display attendance
show_button = driver.find_element(By.ID,"btnShow")
show_button.click()

# wait for the page to load
time.sleep(2)

# output the screen
print(driver.page_source)

time.sleep(3)

till_now_option = driver.find_element(By.ID,"radPeriod")
till_now_option.click()

# to get Today's Date
today=datetime.date.today()

# to convert date into DD/MM/YYYY formate 
today_str=today.strftime("%d/%m/%Y")

# find the FromDate and ToDate input fields and enter the today's Date
user_name = driver.find_element(By.ID, 'txtFromDate')
user_name.send_keys(today_str)

password = driver.find_element(By.ID, 'txtToDate')
password.send_keys(today_str)

# click the "Show" button to display attendance
show_button = driver.find_element(By.ID,"btnShow")
show_button.click()

time.sleep(10)

# close the browser
driver.quit()
