class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def checkbalance(self):
        print("Your balance is: 5000")
    def withdrawl(self,amount):
        remainingamount = 5000 - amount
        print("your remaining balance is: "+ str(remainingamount))

def main():
    card_number=input("insert you cardnumber:  ")
    pinnumber=input("insert you pinnumber: ")

    newuser=Atm (card_number,pinnumber)
    print("chose your activity")
    print("1.balance inquiry 2.withdrawl")
    activity=int(input("enter activity number"))
    if (activity==1):
        newuser.checkbalance()
    elif(activity==2):
        amount=int(input("Enter the amount:  "))
        newuser.withdrawl(amount)
    else:
        print("Enter a valid number")

    
if __name__=="__main__":
    main()