import json
import requests

"""
Description: Currency exchange terminal application with json and requests
"""

api_key="dasds21312423dfdsdf45345345342342ada"
api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/" 


brokenexchangerate=input("Which exchange rate would you like to change? ")
exchangeratetobereceived=input("Which exchange rate would you like? ")
amount=int(input("enter the amount: "))



result=requests.get(api_url+brokenexchangerate) 

result_json=json.loads(result.text)




print("1 {0} = {1} {2}".format(brokenexchangerate,result_json["conversion_rates"][exchangeratetobereceived],exchangeratetobereceived))
print("{0} {1} = {2} {3}".format(amount,brokenexchangerate,amount * result_json["conversion_rates"][exchangeratetobereceived],exchangeratetobereceived))