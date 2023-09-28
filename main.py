from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import re
import gas

url = "https://yandex.ru/metro/moscow?scheme_id=sc34974011"
good_st = "scheme-objects-view__label"
bad_st = "scheme-objects-view__label _warning"
xpath_from = "/html/body/div[2]/div/div[2]/div[3]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/div/span/span/input"
xpath_from_cl = "/html/body/div[6]/div/div/div/div/div[1]/ul/div"
xpath_to = "/html/body/div[2]/div/div[2]/div[3]/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/span/span/input"
xpath_to_cl = "/html/body/div[6]/div/div/div/div/div[1]/ul/div"
xpath_result = "/html/body/div[2]/div/div[2]/div[3]/div/div/div[1]/div[3]/div/div/div[1]/div[1]"

def count_dist(start_station="Лужники", final_station="Спортивная"):
    #print(start_station, final_station)
    #print(xpath_to, xpath_from, xpath_result)
    element1 = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_from)))
    element1.send_keys(start_station)
    #time.sleep(0.05)
    element1.send_keys(Keys.ENTER)
    element2 = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_to)))
    element2.send_keys(final_station)
    #time.sleep(0.05)
    element2.send_keys(Keys.ENTER)
    element3 = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_result)))
    res = 0
    if 'ч' in element3.text and 'мин' in element3.text:
        str = element3.text.split(' ')
        res += int(str[0])*60 + int(str[2])
    elif 'ч' in element3.text:
        str = element3.text.split(' ')
        res += int(str[0])*60
    else:
        res += int(element3.text[:-3:])
    element1.send_keys(Keys.COMMAND + "A")
    #time.sleep(0.1)
    element1.send_keys(Keys.DELETE)
    element2.send_keys(Keys.COMMAND + "A")
    #time.sleep(0.1)
    element2.send_keys(Keys.DELETE)
    return res

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument('--headless')
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 50)
driver.get(url)
time.sleep(3)
count_dist()
df = pd.read_csv("all_stations.csv")
par = pd.read_csv("parameters.csv")
mn = 1000000
ans = ""
for f in df['Station']:
    dist = []
    if mn < 10:
        break
    for s in par['Station']:
        dist.append(count_dist(f, s))
    if mn > max(dist) - min(dist):
        mn = max(dist) - min(dist)
        ans = f
print(ans)
#dist = {}
#for f in df['Station']:
#    dist[f] = []
#    for s in df['Station']:
#        if s != f:
#            dist[f].append([s, count_dist(f, s)])
#        else:
#            dist[f].append([f, 0])
#df_dist = pd.DataFrame(dist)
#df_dist.to_csv("distances.csv", encoding='utf-8', index=False)
#print(df_dist)
driver.close()
driver.quit()
