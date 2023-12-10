import random


user_detail={"email":"xyz@gmail.com","password":"Xyz@123"}

company={"Amazon":5,
         "Flikcart":30,
         "Masho":10}



products = {
        'laptop': 12000,
        'smartphone': 8000,
        'headphones': 1000,
        'smartwatch': 2500,
        'camera': 50000,
        'gaming Console': 300000,
        'Tablet': 40000,
        'Bluetooth Speaker': 2000,
        'Coffee Maker': 600,
        'Blender': 4000,
        'Microwave Oven': 12000,
        'Refrigerator': 8000,
        'Vacuum Cleaner': 2000,
        'Hair Dryer': 300,
        'Toaster': 2500,
        'Air Purifier': 1500,
        'Robot Vacuum': 25000
    }

Cart={}

payment={
    "Gpay":{
        "name":"SBI bank","balance":500000,"pin":1234
    },
    "phonePay":{
        "name":"CBI bank","balance":50000,"pin":4567
    },
    "Debit card":{
            "name":"Axis bank","balance":400000,"pin":5678
    },
    "credit card":{
    "name":"Kotak bank","balance":100000,"pin":2345
    }}

def cart(productName,price,companyName):
    try:
        for i,j in company.items():
            if i==companyName:
                discount=price*j/100
                print(f"{productName} | Discount : ({j}%): {discount} | Origin Price : {price} | Discount Amount :{price-discount}")
                Cart[productName]=price-discount
    except:
        print("Invalid Name")

cart("Toaste",2500,"Amzon")

def Getcompany():
    for key,value in company.items():
        print(f"{key} have {value} %  Discount")


def showCart():
    print("cart Details")
    max_lenght=max(len(key) for key in Cart.keys())
    for key,value in Cart.items():
        key_str=f"{key}"
        justifed_key=key_str.ljust(max_lenght +1)
        print(f"{justifed_key} :{value}")
    print("--------------------------")


def showProducts():
    max_lenght = max(len(key) for key in products.keys())
    for key, value in products.items():
        key_str = f"{key}"
        justifed_key = key_str.ljust(max_lenght + 1)
        print(f"{justifed_key} :{value}")


def TotalAmount():
    value=Cart.values()
    return (sum(value))



def amountAvailable(PaymentWay):
    try:
        global bank_balance
        bank_balance=0
        for i,j in payment.items():
            a = "balance"
            b = "name"
            pin="pin"
            if i==PaymentWay:
                print(f"PinCode : {payment[PaymentWay][pin]}")
                if payment[PaymentWay][pin]==int(input(f"Enter the pin for {payment[PaymentWay][b]} account : ")):
                    print(f"{PaymentWay} is linked to {payment[PaymentWay][b]}")
                    print(f"{payment[PaymentWay][b]} has balance of Rs.{payment[PaymentWay][a]}")
                    bank_balance = payment[PaymentWay][a]
    except:
        print(f"invalid PaymentWay : {PaymentWay} ")
    finally:
        return bank_balance

def paymentDetails():
    print("Payment Details")
    print(payment.keys())
    PaymentWay = input("Payment Way: ")
    bank_balance = amountAvailable(PaymentWay)
    print(bank_balance)

# amountAvailable("Gpay")
# print(payment["Gpay"]["balance"])
# bank_balance = amountAvailable("Gpay")
# print(bank_balance)

def mainprogram():
    # bank_balance = 200000
    try:
        email = input("Enter email:")
        password = int(input("Enter Password: "))
        if email==user_detail["email"] and password==user_detail["password"]:
            print("Login Successfully")
            ans = "yes"
            print()
            # choose the company you want to buy with
            Getcompany()
            companyName = input("Enter Company: ")
            showProducts()
            print()
            while ans.lower() != "no":
                productName = input("Product Name: ")
                if productName is not products.keys():
                    cart(productName, products[productName], companyName)
                    print(productName, " Add successfully")
                else:
                    print("Invalid product")
                ans = input("Do u want to add Product(yes/No): ")
                print()

            print()
            # show the cart
            showCart()
            print("Total Payment : ", TotalAmount())
            print()


            # opt code
            try:
                print("Comform the order !")
                PassOpt = random.randint(1000, 5000)
                print("OTP :", PassOpt)
                opt = int(input("Enter Otp: "))
            except:
                print("Error")

            try:
                if PassOpt == opt:
                    print("Order is place successfully ! ")
                    print()

                    # payment details
                    paymentDetail()
                    count=0
                    try:
                        if bank_balance >= int(TotalAmount()) and bank_balance != 0:
                                print("Bank details :")
                                print("Amount Avaiable : ", bank_balance)
                                bank_balance -= int(TotalAmount())
                                print("Total Payment : ", TotalAmount())
                                print("Remainning Balance :", bank_balance)
                                print()
                                print("Transation Successfully done")
                        else:

                            print("Amount is not there ")
                    except:
                        count += 1
                        print("Please select another Payment Gateway Due to insufficient Balance")
                        paymentDetail()
            except:
                 print("Opt invalid")
        else:
            print("Invaild user or password ")

    except ValueError as n:
        print(n)



mainprogram()


