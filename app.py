# Selenium
from selenium import webdriver
print("1")
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from helium import *
print("2")
import time
print("3")
from flask import Flask,render_template
import webbrowser
import threading,webbrowser
app = Flask(__name__)

uid = input('学籍番号を入力してください')
pw = input('パスワードを入力してください')

print("4")
driver = start_chrome('https://navi.mars.kanazawa-it.ac.jp/portal/student/')
print("5")
driver.find_element(by=By.NAME,value="uid").send_keys(uid)
driver.find_element(by=By.NAME,value="pw").send_keys(pw)
driver.find_element(by=By.ID,value="StudentLoginBtn").click()
driver.find_element(by=By.CLASS_NAME,value="crrclmFlow").click()
time.sleep(2)
print("6")
elements = driver.find_elements(By.CLASS_NAME, "kmkLine.rsColor.nn2023")
# print(elements)
tabunyarusyukudai_name = []
tabunyarusyukudai_time = []
for element in elements[::-1]:
    # print(element)
    try:
        #element.ActionChains()
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()

        # ここで取得した情報を処理するコードを記述
        driver.switch_to.window(driver.window_handles[1])
        # print(get_driver().current_url)
        time.sleep(1)
        elementses = driver.find_elements(By.TAG_NAME, "a")
        # print(elementses)
        for elementes in elementses:
            # print(elementes,elementes.get_attribute("href"))
            if "execReport" in str(elementes.get_attribute("href")):
                elementes.click()
                time.sleep(0.3)
                table = driver.find_element(By.CLASS_NAME, "JugyoSummary")
                trs = table.find_elements(By.TAG_NAME, "tr")
                tdstext = []
                for i in range(1, len(trs)):
                    tds = trs[i].find_elements(By.TAG_NAME, "td")
                    for td in tds:
                        tdstext.append(td.text)
                    if "提出済" in tdstext:
                        name = tdstext[0]
                        term  = tdstext[2]
                        print(name, term)
                        tabunyarusyukudai_name.append(name)
                        tabunyarusyukudai_time.append(term)
                click("閉じる")
        driver.close()#タブを閉じる
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(f'Error: {e}')
        continue
    
from datetime import datetime
# 現在の日時を取得
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
datetime_obj = datetime.strptime(formatted_time, "%Y-%m-%d %H:%M:%S")
# 年、月、日、時、分、秒を取得
year = datetime_obj.year
month = datetime_obj.month
day = datetime_obj.day
hour = datetime_obj.hour
minute = datetime_obj.minute
second = datetime_obj.second
# print(formatted_time)
yarusyukudai_name = []
yarusyukudai_time = []
import re
pattern = r"(\d{4}/\d{2}/\d{2} \d{2}:\d{2})～(\d{4}/\d{2}/\d{2} \d{2}:\d{2})"
for i in range(len(tabunyarusyukudai_name)):
    print(tabunyarusyukudai_name,tabunyarusyukudai_time)
    match = re.search(pattern, tabunyarusyukudai_time[i])
    # 開始日時と終了日時を取得
    start_datetime_str = match.group(1)
    end_datetime_str = match.group(2)
    # 開始日時と終了日時をdatetimeオブジェクトに変換
    start_datetime = datetime.strptime(start_datetime_str, "%Y/%m/%d %H:%M")
    end_datetime = datetime.strptime(end_datetime_str, "%Y/%m/%d %H:%M")
    end_year = end_datetime.year
    end_month = end_datetime.month
    end_day = end_datetime.day
    end_hour = end_datetime.hour
    end_minute = end_datetime.minute
    end_second = end_datetime.second
    # if end_year > year and end_month > month and end_day > day and end_hour > hour and end_minute > minute and end_second > second:
    yarusyukudai_name.append(tabunyarusyukudai_name[i])
    yarusyukudai_time.append(end_datetime)
#    except ZeroDivisionError:
#     print('Error')
print("7")
print(yarusyukudai_name, yarusyukudai_time)
#for risyunow in risyunows:
#    print(risyunow)
#driver.switch_to.new_window("https://mars41.mars.kanazawa-it.ac.jp/eSylla/eSRefSummaryPortalAuth")
#click('場所を指定')
#write("Python", into = "")
#driver.close()#タブを閉じる
time.sleep(10)
driver.quit()
@app.route("/")
def index():
    return render_template("index.html",data = zip(yarusyukudai_name,yarusyukudai_time))
if __name__ == "__main__":
    threading.Timer(1.0, lambda: webbrowser.open('http://localhost:5000') ).start()
    app.run(debug=False)
#
# from flask import Flask,render_template
# import webbrowser
# import threading,webbrowser
# app = Flask(__name__)
# # 課題名,提出期限
# # a1= [...]
# # a2 = [....]
# # a2の中の日付をソートする
# a1=yarusyukudai_name
# a2=yarusyukudai_time
# @app.route("/")
# def index():
#     return render_template("index.html",data = zip(a1,a2))
# if __name__ == "__main__":
#     threading.Timer(1.0, lambda: webbrowser.open('http://localhost:5000') ).start()
#     app.run(debug=False)
# print(html)















# # Selenium
# from selenium import webdriver
# print("1")
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from helium import *
# print("2")
# import time
# print("3")
# from flask import Flask,render_template
# import webbrowser
# import threading,webbrowser
# app = Flask(__name__)

# driver = webdriver.Chrome()
# print("4")
# driver = start_chrome('https://navi.mars.kanazawa-it.ac.jp/portal/student/')
# print("5")
# driver.find_element(by=By.NAME,value="uid").send_keys("1318913")
# driver.find_element(by=By.NAME,value="pw").send_keys("Tataiga0814")
# driver.find_element(by=By.ID,value="StudentLoginBtn").click()
# driver.find_element(by=By.CLASS_NAME,value="crrclmFlow").click()
# #start_chrome('https://navi.mars.kanazawa-it.ac.jp/portal/student/KITP00500')
# time.sleep(1)
# print("6")

# click("[必修]")

# time.sleep(3)
# a = driver.find_elements(By.TAG_NAME, "a")
# # print(a)
# # print(elements)
# print("7")

# name = ""
# term = ""
# # 課題名,提出期限
# # a1= [...]
# # a2 = [....]
# # a2の中の日付をソートする
# a1=[]
# a2=[]

# for href in a:
#     # print(str(href.get_attribute("href")))
#     if "execReport" in str(href.get_attribute("href")):
#         href.click()
#         time.sleep(1)

#         table = driver.find_element(By.CLASS_NAME, "JugyoSummary")
#         trs = table.find_elements(By.TAG_NAME, "tr")
#         tdstext = []

#         for i in range(1, len(trs)):
#             tds = trs[i].find_elements(By.TAG_NAME, "td")
#             for td in tds:
#                 tdstext.append(td.text)
#             if "提出済" in tdstext:
#                 name = tdstext[0]
#                 term  = tdstext[2]
#                 a1.append(str(name))
#                 a2.append(str(term))

# print("8")
# print(a1, a2)

# @app.route("/")
# def index():
#     return render_template("index.html",data = zip(a1,a2))
# if __name__ == "__main__":
#     threading.Timer(1.0, lambda: webbrowser.open('http://localhost:5000') ).start()
#     app.run(debug=False)

# print("9")
# #elem_href = elem.find_element_by_tag_name('a').get_attribute('href')
# #risyunows = driver.find_elements(by=By.CLASS_NAME, value="kmkLine rsColor nn2023")
# #print(risyunows)
# #for risyunow in risyunows:
# #    print(risyunow)
# #driver.switch_to.new_window("https://mars41.mars.kanazawa-it.ac.jp/eSylla/eSRefSummaryPortalAuth")
# #click('場所を指定')
# #write("Python", into = "")
# #driver.close()#タブを閉じる
# time.sleep(100)
# driver.quit()