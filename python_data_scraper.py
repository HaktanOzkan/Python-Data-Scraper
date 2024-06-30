import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.bloomberght.com/piyasalar"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

session = requests.Session()
session.headers.update(headers)

response = session.get(url)

soup = BeautifulSoup(response.text, "html.parser")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    data_div = soup.find_all("div", attrs={"class":"widget-markets-chart"})
    
    if data_div:
        with open('market_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Name', 'Bulk Value'])  # Header
            for names in data_div:
                name = names.a.text.strip()
                bulk_value = names.find("span", attrs={"class":"bulk"}).text.strip()
                csvwriter.writerow([name, bulk_value])
            print("Veriler market_data.csv dosyasına kaydedildi.")

    else:
        print("Hata: Belirtilen sınıfa sahip <div> bulunamadı.")
else:
    print(f"Hata: URL'e erişim sağlanamadı, HTTP durum kodu: {response.status_code}")