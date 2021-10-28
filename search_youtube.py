import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def search_youtube(search_key):
    driver_opt = Options()
    driver_opt.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=driver_opt)
    driver.get("http://www.youtube.com")
    driver.implicitly_wait(15)
    driver.find_element(By.CSS_SELECTOR, "tp-yt-paper-button[aria-label='Agree to the use of cookies and other data for the purposes described']").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.NAME, "search_query")))
    search = driver.find_element(By.NAME, "search_query")
    search.click()
    search.send_keys(search_key)
    search.submit()

    driver.implicitly_wait(10)

    links = driver.find_elements(By.XPATH, '(//a[@id="thumbnail"])')

    random_link = random.randrange(0, len(links))
    if links[random_link] is not None:
        links[random_link].click()

    assert "No results found." not in driver.page_source
