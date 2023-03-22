from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
options = webdriver.ChromeOptions()
options.add_argument('-headless')
options.add_argument('-no-sandbox')
options.add_argument('-disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# driver.get("https://tiki.vn/")
# cats = driver.find_elements(By.CLASS_NAME,"cjqkgR")[1].find_elements(By.TAG_NAME,"a")
# catDict = {cat.get_attribute("href"):cat.get_attribute("textContent") for cat in cats}
# for key,val in catDict.items():
#     print(key,val)



val = "mevabe"
def getProduct(prod):
    cat = val
    name = prod.find_element(By.CLASS_NAME,"name").get_attribute("textContent")
    rating = prod.find_elements(By.CLASS_NAME,"full-rating")
    if len(rating) == 1:
        rating = rating[0].get_attribute("textContent")
    else:
        rating = None
    if (len(prod.find_elements(By.CLASS_NAME,"fCfYNm")) == 1):
        sold = prod.find_element(By.CLASS_NAME,"fCfYNm").get_attribute("textContent").replace("Đã bán ","")
    else:
        sold = 0
    price = prod.find_element(By.CLASS_NAME,"price-discount__price").get_attribute("textContent").replace(" ₫","")
    img = prod.find_element(By.CLASS_NAME,"image-wrapper").find_element(By.TAG_NAME,"img").get_attribute('src')
    if (prod.find_elements(By.CLASS_NAME,"price-discount__discount") == 1):
        discount = prod.find_element(By.CLASS_NAME,"price-discount__discount").get_attribute("textContent").replace("-","")
    else:
        discount = 0
    if (len(prod.find_element(By.CLASS_NAME,"thumbnail").find_elements(By.TAG_NAME,"img")) == 2):
        verify = prod.find_element(By.CLASS_NAME,"thumbnail").find_element(By.TAG_NAME,"img").get_attribute('alt')
    else:
        verify = None
    deliStatus = prod.find_element(By.CLASS_NAME,"badge-delivery").get_attribute("textContent")
    return {"name":name,"category":cat,"image":img,"price":price,"sold":sold,"rating":rating,"verify":verify,
              "discount":discount,"delivery_status":deliStatus}

def getListsProduct(link):
    driver.get(link)
    sleep(1)
    prodList = []
    prods = driver.find_elements(By.CLASS_NAME,"product-item")
    for i in range(150):
        driver.execute_script("window.scrollTo(0, window.scrollY + 20)")
    for prod in prods:
        prodList.append(getProduct(prod))
    return prodList

print(getListsProduct("https://tiki.vn/san-pham-tai-chinh-bao-hiem/c54042"))