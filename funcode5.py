class Bank:
    def __init__(self,AccNo,pin="1473"):
        self.AccNo=AccNo
        self.pin=pin
    BankName="SBI"
b1=Bank(1357)
b2=Bank(1257,"1234")
print(b1)
print(b1.AccNo)
print(b2.AccNo)
b1.Bankname="Union"
b2.Bankname="HDFC"