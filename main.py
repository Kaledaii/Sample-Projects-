from requests import get
from pprint import PrettyPrinter


API_KEY="4680fd73201869b9b7b7477d"
convert="https://v6.exchangerate-api.com/v6/4680fd73201869b9b7b7477d/pair/"
#"https://v6.exchangerate-api.com/v6/4680fd73201869b9b7b7477d/pair/USD/EUR/100"
printer=PrettyPrinter()
def get_currencies():
    url="https://v6.exchangerate-api.com/v6/4680fd73201869b9b7b7477d/latest/USD"
    data=get(url).json()['conversion_rates']
    data=list(data.items())
    return data

data=get_currencies()
printer.pprint(data)
def exchange_rate():
    BASE_currency="USD"
    TARGET_currency=input("Enter the code for target currency: ").upper()
    convert=f"https://v6.exchangerate-api.com/v6/4680fd73201869b9b7b7477d/pair/{BASE_currency}/{TARGET_currency}"
    response=get(convert).json()
    response=response['conversion_rate']
    print(f'{BASE_currency} -> {TARGET_currency} ={response}')
    print('The conversion rate is ',response)
    print("\nFor conversion:")
    print(f'\n 1.USD -> {TARGET_currency} \n 2.{TARGET_currency} -> USD')
    return response,TARGET_currency

rate,TARGET_currency=exchange_rate()

def cost(rate,TARGET_currency):
    ans=int(input("Choose 1 or 2 for conversion "))
    if ans==1:
        amt=float(input("How much USD do you want to convert ? " ))
        get=round(amt*rate,2)
        print(f'USD({amt}) = {TARGET_currency}({get})')
    else:
        print(f"How much {TARGET_currency} do you want to convert to USD ?")
        amt=float(input())
        get=round(amt/rate,2)
        print(f'{TARGET_currency}({amt}) = USD({get})')

cost(rate,TARGET_currency)