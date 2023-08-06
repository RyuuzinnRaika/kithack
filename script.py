# Selenium
from selenium import webdriver
print("1")
from selenium.webdriver.common.by import By
from helium import *
print("2")
import time
print("3")
#driver = webdriver.Chrome()
print("4")
driver = start_chrome('https://navi.mars.kanazawa-it.ac.jp/portal/student/')
print("5")
driver.find_element(by=By.NAME,value="uid").send_keys("1304271")
driver.find_element(by=By.NAME,value="pw").send_keys("ryuuzinnryuu")
driver.find_element(by=By.ID,value="StudentLoginBtn").click()
driver.find_element(by=By.CLASS_NAME,value="crrclmFlow").click()
#start_chrome('https://navi.mars.kanazawa-it.ac.jp/portal/student/KITP00500')
time.sleep(2)
print("6")
#click(Image("td.kmkLine.rsColor.nn2023"))
elements = driver.find_elements(By.CLASS_NAME, "kmkLine.rsColor.nn2023")
print(elements)

for element in elements:
    print(element)
    try:
        time.sleep(1)
        element.click()
    except ZeroDivisionError:
        print('Error')
    except Exception as e:
        print(f'Error: {e}')
    # ここで取得した情報を処理するコードを記述
print("7")
risyunows = driver.find_elements(by=By.CLASS_NAME, value="kmkLine rsColor nn2023")
print(risyunows)
#for risyunow in risyunows:
#    print(risyunow)
#driver.switch_to.new_window("https://mars41.mars.kanazawa-it.ac.jp/eSylla/eSRefSummaryPortalAuth")
#click('場所を指定')
#write("Python", into = "")
#driver.close()#タブを閉じる
time.sleep(100)
driver.quit()