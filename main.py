from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import *
import time

chrome_driver_path = "C:/Users/brian/Documents/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2347340420&distance=50&f_LF=f_AL&f_TPR=a1608737471-&geoId=100354078&keywords=python&location=Imperial%2C%20Missouri%2C%20United%20States")
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()
time.sleep(1)
username = driver.find_element_by_id("username")
username.send_keys("brian.whiteley@att.net")
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
log_in_button = driver.find_element_by_tag_name("button")
log_in_button.click()
time.sleep(1)
job_list = driver.find_elements_by_class_name("job-card-list__title")
for job in job_list:
    job.click()
    time.sleep(5)
    apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
    apply_button.click()
