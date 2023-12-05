import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selectorlib 
from bs4 import BeautifulSoup
import pandas as pd
import time 
import json





#URL = "https://www.vrbo.com/search?adults=2&amenities=&children=&d1=2023-12-06&d2=2023-12-07&destination=73rd%20Ave%2C%20Queens%2C%20NY%2C%20USA&endDate=2023-12-15&latLong=&mapBounds=&pwaDialog=&regionId&semdtl=&sort=RECOMMENDED&startDate=2023-12-14&theme=&userIntent="
def scrape(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    driver.execute_script("document.getElementsByClassName('uitk-layout-grid-item uitk-scrollable uitk-scrollable-vertical')[0].scrollTop += 5*document.body.scrollHeight;")
    time.sleep(5) # wait for content to load
    
    
    source = driver.page_source
    driver.quit()
    return source

def dfToJson(df):
    res = df.to_json(orient="records")
    parsed = json.loads(res)
    return parsed

def extract(source, max_distance):
    names = []
    links=[]
    prices=[]
    distances=[]
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['list']
    soup = BeautifulSoup(value, 'html.parser')
    list_div = soup.find('div', {'data-stid': 'property-listing-results'})
    child_divs = list_div.find_all('div', class_='uitk-spacing uitk-spacing-margin-blockstart-three')
    for child_div in child_divs:
        if child_div:
            child1 = child_div.find('div', {'data-stid': 'lodging-card-responsive'})
            print("child1")
            if child1:
                child2 = child1.find('div', class_="uitk-layout-grid uitk-layout-grid-has-auto-columns uitk-layout-grid-has-columns-by-medium uitk-layout-grid-display-grid")
                linkref = child1.find('a', {'data-stid': 'open-hotel-information'})['href']
                link = "https://www.vrbo.com" + linkref
                if link:
                    links.append(link)
                    print("link")

                print("child2")
                if child2:
                    child3 = child2.find('div', class_="uitk-card-content-section uitk-card-content-section-padded uitk-layout-grid-item uitk-layout-grid-item-has-column-start-by-medium").find('div', class_="uitk-layout-flex uitk-layout-flex-block-size-full-size uitk-layout-flex-flex-direction-column uitk-layout-flex-justify-content-space-between")
                    print("child3")
                    if child3:
                        price1=child3.find('div',class_="uitk-layout-grid uitk-layout-grid-has-auto-columns uitk-layout-grid-has-columns uitk-layout-grid-has-columns-by-medium uitk-layout-grid-has-columns-by-large uitk-layout-grid-has-space uitk-layout-grid-display-grid uitk-layout-flex-item")
                        price2=price1.find('div',class_="uitk-layout-flex uitk-layout-flex-flex-direction-column uitk-layout-grid-item uitk-layout-grid-item-align-self-end uitk-layout-grid-item-has-column-start uitk-layout-grid-item-justify-self-end")
                        price3=price2.find('div',{'data-test-id':'price-summary'}).find('div',{'data-test-id':'price-summary-message-line'})
                        price4=price3.find('div',class_="uitk-spacing uitk-spacing-padding-block-half")
                        price=price4.find('div',class_="uitk-text uitk-type-500 uitk-type-medium uitk-text-emphasis-theme")

                        name_dist = child3.find('div', class_="uitk-spacing uitk-spacing-padding-blockend-three uitk-layout-flex-item").find('div', class_="uitk-layout-grid uitk-layout-grid-has-auto-columns uitk-layout-grid-has-rows uitk-layout-grid-display-grid uitk-layout-flex-item")
                        print("namedist")
                        if name_dist:
                            # name = name_dist.find('h3', class_="uitk-heading uitk-heading-5 overflow-wrap uitk-layout-grid-item uitk-layout-grid-item-has-row-start")
                            # print("name")
                            distance=name_dist.find('div',class_="uitk-layout-flex uitk-layout-flex-align-items-center uitk-layout-flex-gap-one").find('div',class_="uitk-text uitk-type-300 uitk-text-default-theme")
                            # if name:
                            #     names.append(str(name.text))
                            #     print("done")
                            if distance:
                                distance_match = re.search(r'\d+(\.\d+)?', str(distance.text))
                                if distance_match:
                                    final_distance = float(distance_match.group())
                                    distances.append(final_distance)
                                    print("distance")

                            if price:
                                prices.append(str(price.text))
                                print("price")
    dict = {'link':links,'distance':distances,'price':prices}
    print (len(links))
    print(len(distances))
    print(len(prices))
    df=pd.DataFrame(dict)
    if max_distance != -1:
        df = df[df['distance'] <= max_distance]
    # sort by distance
    df = df.sort_values(by='distance')
    return df

# if __name__ == "__main__":
#     source = scrape(URL)
#     # extract(source)
#     # with open("output.html", 'w', encoding='utf-8') as f:
#     #     f.write("\n".join(extract(source)))
#     df=extract(source)
#     df.to_csv('op.csv')
#     print(df.head())

def main(destination="New Delhi",distance=-1):
    base_url = "https://www.vrbo.com/search"

    # Hardcoded parameters
    adults = 2
    amenities = ""
    children = ""
    start_date = "2023-12-14"
    end_date = "2023-12-15"
    sort = "RECOMMENDED"

    # Constructing the URL with hardcoded parameters
    URL = f"{base_url}?adults={adults}&amenities={amenities}&children={children}&startDate={start_date}&endDate={end_date}&destination={destination}&sort={sort}"
    source = scrape(URL)
    df=extract(source=source, max_distance=distance)
    df.to_csv('op.csv')
    return dfToJson(df)
