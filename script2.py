
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium WebDriver (make sure to replace with the appropriate driver)
driver = webdriver.Chrome()

# Load the webpage
url =  "https://www.vrbo.com/search?adults=2&amenities=&children=&d1=2023-11-19&d2=2023-11-20&destination=The%20Loop%2C%20Chicago%2C%20Illinois%2C%20United%20States%20of%20America&endDate=2023-12-05&latLong=41.883736%2C-87.62886&mapBounds=&pwaDialog=&regionId=800024&semdtl=&sort=RECOMMENDED&startDate=2023-12-04&theme=&userIntent="

driver.get(url)

# Define the XPath of the list containing all properties
list_xpath = '//*[@id="app-layer-base"]/div[1]/div[4]/div[1]/div[2]/div[3]'

try:
    # Wait for the list element to be present
    list_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, list_xpath))
    )

    # Loop over each property and extract the name
    for i in range(1, len(list_element.find_elements(By.XPATH, 'div')) + 1):
        property_xpath = f'{list_xpath}/div[{i}]/div/div/div/div[2]/div/div[1]/div[1]/div/h3'
        
        # Find the name element for each property
        name_element = driver.find_element(By.XPATH, property_xpath)
        
        # Extract and print the name
        property_name = name_element.text
        print(f"Property {i} Name: {property_name}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the WebDriver
    driver.quit()
