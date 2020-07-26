from urllib.request import urlopen
from bs4 import BeautifulSoup
import time


def getData():
    html = urlopen("https://www.bloomberght.com/doviz").read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


class DovizBirim:
    def __init__(self, name, className):
        self.name = name
        self.className = className

    def getDovizData(self, soup):
        liContainer = soup.find("li", {"class": self.className})
        currencyValue = liContainer.find(
            "small", {"class": "value LastPrice"}).text
        currencyChangeinPercentage = liContainer.find(
            "small", {"class": "value-diff upGreen PercentChange"}).text.replace(" ", "").replace("\n", "")
        increasing = True if str(liContainer.find(
            "i", {"class", "data-icon up"})) != "None" else False
        print("Anlık {name} Kuru : {dolarKuru} ve yüzdelik {yuzdeDegisim} ile {increasing}".format(
            name=self.name, dolarKuru=currencyValue, yuzdeDegisim=currencyChangeinPercentage, increasing="artmakta" if increasing == True else "düşüşte"))


while True:
    dolar = DovizBirim("Dolar", "live-dolar")
    dolar.getDovizData(getData())
    euro = DovizBirim("Euro", "live-euro")
    euro.getDovizData(getData())
    borsa = DovizBirim("Borsa Ist", "live-bist-100")
    borsa.getDovizData(getData())
    faiz = DovizBirim("Faiz", "live-faiz")
    faiz.getDovizData(getData())
    altin = DovizBirim("Altın", "live-altin-ons")
    altin.getDovizData(getData())
    print("-----------------------------------------------\n")
    time.sleep(10)
    
