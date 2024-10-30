from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = "adam880614@gmail.com"
password = "7378736501156753"

driver = webdriver.Chrome()

#直接進入限動的話可以少很多步驟
driver.get("https://www.instagram.com/stories/adam0614__/")

time.sleep(2)
wait = WebDriverWait(driver, 20)

#登入
driver.find_element(By.NAME,"username").send_keys(username)
driver.find_element(By.NAME,"password").send_keys(password)
driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
driver.switch_to.window(driver.window_handles[-1])

#處理彈出視窗
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '稍後再說')]"))).click()
driver.switch_to.window(driver.window_handles[-1])

#點出有誰看過
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="xzueoph"]'))).click()
driver.switch_to.window(driver.window_handles[-1])

try:
    names = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1")))
    for name in names:
        print(name.text)
    print('y')
except:
    print('e')