import time
from selenium import webdriver

driver = webdriver.Chrome()
start = time.time()
driver.get("https://www.youtube.com/watch?v=Kt2AzLPoljI")
end = time.time()
print("Time taken: "+ str(end-start))
driver.quit()
