# opening a file

# f = open("src/Currencyconvertor using _Python/main.txt", "r")

# print(f.read())


# for lines in f:
#     parsed = f.split("\t")

#     print(parsed)


from forex_python.converter import CurrencyRates


from forex_python.converter import CurrencyCodes


cr = CurrencyRates()

amount = int(input("\n Please enter the amount you want to convert"))

from_currency = input("Please enter the currency code that has to be converted").upper()

to_currency = input("Please enter the currency code  to convert").upper()

print("You are converting from ", amount, from_currency, "to", to_currency, " ")

output = cr.convert(from_currency, to_currency, amount)

print("The converted rate is ", output)
