import requests

print(" [+]  Author    : Rianda Fuad Shafly")
print(" [+]  Info      : ShortLink Generator")
print(" [+]  Website   : www.riandafuadshafly.my.id")
print(" [+]  Contact   : bangrianda456@gmail.com")
print(" ---------------------------------------------")
linkmu = input(" [?]  Masukkan Link : ")
def main(pendek):
      url = "https://jar-api.xyz/api/short/tiny?url={}&apikey=aichan".format(linkmu)
      data = requests.get(url).json()
      short = data['result']['link']
      print(" [-]  ShortLink : " + short)
      
main(linkmu)
