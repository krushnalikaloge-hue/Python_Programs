class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Name :", self.Name)
        print("Balance :", self.Amount)

    def Deposit(self):
        Money = int(input("Enter Deposit Amount : "))
        self.Amount = self.Amount + Money

    def Withdraw(self):
        Money = int(input("Enter Withdraw Amount : "))
        if Money <= self.Amount:
            self.Amount = self.Amount - Money
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest :", Interest)


obj1 = BankAccount("Sanket", 10000)

obj1.Display()
obj1.Deposit()
obj1.Display()
obj1.Withdraw()
obj1.Display()
obj1.CalculateInterest()