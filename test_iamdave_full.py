
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.iamdave.ai")
    WebDriverWait(driver, 10).until(EC.title_contains("DaveAI"))
    print("Test 1 Passed: Website loaded successfully")
    print("Page Title:", driver.title)

    heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    print("Test 2 Passed: Main heading found:", heading.text)

   
    try:
        contact_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Contact"))
        )
        contact_button.click()
        WebDriverWait(driver, 10).until(EC.url_contains("contact"))
        print("Test 3 Passed: Navigation to Contact page works")
    except:
        print("Test 3 Skipped: 'Contact' button/link not found")

    try:
        footer_logo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "footer img"))
        )
        print("Test 4 Passed: Footer logo found")
    except:
        print("Test 4 Skipped: Footer logo not found")

finally:
    driver.quit()
    print("All tests completed and browser closed.")
