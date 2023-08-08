import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

FILENAME = "data.csv"
HEADERS = ["Provinsi", "Kab/Kota", "Tipe", "Kecamatan", "Kode Wilayah"]
with open(FILENAME, "w") as f:
    write = csv.writer(f)
    write.writerow(HEADERS)

driver.get("https://nomor.net/")
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
tables = soup.find_all(attrs={"bgcolor": "#ccffff"})
for t in tables:
    encoded_province_url = t.td.next_sibling.a["href"].replace(" ", "%20")
    province_name = t.td.next_sibling.a.text
    print(province_name)
    driver.get(encoded_province_url)
    province_content = driver.page_source
    province_soup = BeautifulSoup(province_content, "html.parser")
    city_table = province_soup.find_all(attrs={"class": "cstr"})
    for c in city_table:
        encoded_district_url = c.td.next_sibling.next_sibling.a["href"].replace(" ", "%20")
        city_type = c.td.next_sibling.text
        city_name = c.td.next_sibling.next_sibling.a.text
        print(city_type)
        print(city_name)
        driver.get(encoded_district_url)
        district_content = driver.page_source
        district_soup = BeautifulSoup(district_content, "html.parser")
        district_data = district_soup.findAll("tr", {"bgcolor": "#ccffff"})
        for dd in district_data:
            data = []
            region_name = dd.td.next_sibling.next_sibling.a.text
            region_code = dd.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text.replace(".", "")
            data.append(province_name)
            data.append(city_name)
            data.append(city_type)
            data.append(region_name)
            data.append(region_code)
            print(region_name + ": " + region_code)

            with open(FILENAME, "a+") as f:
                write = csv.writer(f)
                write.writerow(data)

driver.quit()
