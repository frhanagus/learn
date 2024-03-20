def check_rate(kurs): 
    #to convert foreign money to IDR
    # 1 USD = 15710
    # 1 JPY = 105
    # 1 EUR = 17000 
    print ('Pilih mata uang yang ingin dibeli: ')
    print ('1. USD\n2. JPY\n3.EUR\n0. Exit')
    print()
    choice = int(input("Pilihan Anda: "))
    
    if choice == 1 :
        rate = 15710
        print ()
        amount = int(input('Input jumlah yang ingin dibeli (dalam USD): '))
        print ()
        print (f'Untuk membeli USD {amount} Anda harus membayar IDR {rate*amount}')

def inputAmount(kurs):
    #to input IDR amount to be converted

def convertCurrency(amount, rate):
    #to convert IDR to foreign money

def printResult(currency, amount, result, currencyResult):
    #to print converted amount

use while True 
# to make the program run till user choose to exit