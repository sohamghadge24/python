class Whatsapp:
    def videoCall(self,name):
        print(f"Whatsapp Video Call to {name}")
    def VoiceCall(self,name):
        print(f"Whatsapp Voice Call  to {name}")
    def chat(self,name):
        print(f"Whatsapp Chat  to {name}")
    def Payment(self,name):
        a=details()
        payee =input("Enter payment mode(sender/receiver) : ")
        if payee == "sender":
            a.sender(name)
            print(f"Payment  to {name} through Whatsapp")
        elif payee=="receiver":
            a.receiver(name)
            print(f"Payment  from {name} through Whatsapp")
        else:
            print("Invalid Option")
    
class Telegram(Whatsapp):
    def __init__(self):
         super.__init__
    def videoCall(self,name):
        print(f"Telegram Video Call to {name}")
    def VoiceCall(self,name):
        print(f"Telegram Voice Call  to {name}")
    def chat(self,name):
        print(f"Telegram Chat  to {name}")
    
class details:
    name=["soham","Rohan","Aayush"]
    bank_balance=1000

    def sender(self,user):
        amount=int(input("Enter Amount You want to Transfer  to : "))
        self.bank_balance-=amount
        print(f'you send Rs.{amount} to {user}')
        print(f'Your Balance is {self.bank_balance}')
        print("Payment successful")

    def receiver(self,user):
        amount=int(input("Enter You receiver Amount : "))
        self.bank_balance+=amount
        print(f'you receiver Rs.{amount} from {user}')
        print(f'Your Balance is {self.bank_balance}')
        print("Payment successful")

    def show_details(self,name):
        for i in range (len(self.name)):
            if name==self.name[i]:
                return self.name[i]
    def get_details(self):
        print("Details of all users are as follows: ")
        for i in range(len(self.name)):
            print(f"{self.show_details(self.name[i])}")
                 
class User(Telegram,Whatsapp,details):
    def __init__(self):
        super.__init__
        self.showUser()
        
    def showUser(self):
        print("Whatsapp \nTelegram ")
        self.App=(input("Enter App name :"))
        print("what do you want to you ?\nvideoCall\nvoiceCall\nchat\npayment")
        self.choice=input("Enter the method : ")
        self.Authentication()

    def user(self):
        self.get_details()
        userName=input("Enter User Name :")
        return self.show_details(userName)

    
    def Authentication(self):
        if self.App=="Whatsapp":
            a=Whatsapp()
            if self.choice=="videocall":
                user1=self.user()
                a.videoCall(user1)
            elif self.choice=="voicecall":
                user1=self.user()
                a.VoiceCall(user1)
            elif self.choice=="chat":
                user1=self.user()
                a.chat(a,user1)
            elif self.choice=="payment":
                user1=self.user()
                a.Payment(user1)
            else:
                print("Invalid Choice")
        else:
            a=Telegram()
            if self.choice=="videocall":
                user1=self.user()
                a.videoCall(user1)
            elif self.choice=="voicecall":
                user1=self.user()
                a.VoiceCall(user1)
            elif self.choice=="chat":
                user1=self.user()
                a.chat(user1)
            else:
                print("Invalid Choice")
    
            

User()
