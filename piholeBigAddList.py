
from selenium import webdriver
import time


print('################################################')
print("use the script if you are confirm with url.txt")
print('################################################')



############ add your PiholeURL ############
piholeURL = input("Your PiHole Adress:")
piholeURL = "http://" + piholeURL

############ Login ############
print(f"Try to login to: {piholeURL}")
password = input("password: ")
driver = webdriver.Chrome()
driver.get(f'{piholeURL}/admin/index.php?login')
login = driver.find_element_by_id("loginpw")
login.send_keys(password)
login.submit()


############ add list ############
url = piholeURL + "/admin/groups-adlists.php"
print(f"Connect to {url}")
driver.get(url)

############ add all URL in your PiHole ############
text = open('url.txt', 'r')

urlField = driver.find_element_by_id('new_address')
commentField = driver.find_element_by_id('new_comment')
addBtn = driver.find_element_by_id('btnAdd')

for line in text:
    if line[0] == '#':
        continue

    urlField.send_keys(line)
    commentField.send_keys('piholeBigAddlist-Script')
    addBtn.click()
    time.sleep(1)

text.close()

############ update ############

url = piholeURL + "/admin/gravity.php"
print(f"Connect to :{url}")
driver.get(url)

updateField = driver.find_element_by_id("gravityBtn")
updateField.click()







