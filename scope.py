balance = 3000

def buy_things(item,price):
    # local scope variable
    #you can access global variable without using the global keyword
    dream_phone = 'xphone'
    #If you want to modify a global variable without using the global keyword
    
    #jodi amra global balance use korte chai taile global like dibo
    global balance

    print(f'previous balance value',balance)
    # balance = 500
     
    balance = balance - price

    print(f'balance after buying {item}',balance)
# print(dream_phone)

buy_things('sunglass',1000)
print('global balance after buy ',balance)

