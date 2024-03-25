from Acount import Acount
import datetime
class privateAcount(Acount):
    """class of publicAcount"""
    numbrerBranche="123"

    def __init__(self,numAcount, sumMonyInAcount,namePerson,deviation):
        super(privateAcount,self).__init__(numAcount,sumMonyInAcount)
        self.namePerson = namePerson
        self.deviation = deviation
        self.addFile(namePerson)

    def cash_withrawal(self,sum):
        """cash withrawal"""
        if self.sumMonyInAcount-sum<-self.deviation:
            print("עברת את המכסה החודש")
        elif self.sumMonyInAcount-sum<0:
            answer=input("האם תרצה להכנס למינוס בחשבונך?")
            if answer=="כן":
                self.sumMonyInAcount-=sum
                print(f"נמשך בהצלחה הסכום הזה:{sum}")
                f = open(f'{self.namePerson}.txt', 'a', encoding='utf-8')
                f.write(f"נמשך בהצלחה הסכום הזה:{sum}\n")
                f.close()
        else:
            self.sumMonyInAcount -= sum
            print(f"נמשך בהצלחה הסכום הזה:{sum}")
            f = open(f'{self.namePerson}.txt', 'a', encoding='utf-8')
            f.write(f"נמשך בהצלחה הסכום הזה:{sum}\n")
            f.close()

    def addFile(self, namePerson):
        """add File"""
        file=open(f'{namePerson}.txt','w',encoding='utf-8')
        file.write(f" שלום ל {namePerson}\n")
        file.write(f"  תודה לך שהצטרפת ל {self.nameBank}\n")
        file.write(f"החשבון נפתח בהצלחה בתאריך: {datetime.date.today()}\n")
        file.close()
    def Deposit_money(self,sum):
        self.sumMonyInAcount += sum
        print(f"  הפקדת בהצלחה את הסכום הזה:{sum}\n")
        f = open(f'{self.namePerson}.txt', 'a', encoding='utf-8')
        f.write(f"הופקד בהצלחה הסכום הזה: {sum}\n")
        f.close()

    def Account_Balance(self):
        print(f"היתרה בחשבונך:  {self.sumMonyInAcount} \n")
        f = open(f'{self.namePerson}.txt', 'a', encoding='utf-8')

        f.write("צפיה בחשבון\n")
        f.close()
    def View_recent_actions(self):
        f = open(f'{self.namePerson}.txt', 'r', encoding='utf-8')
        print(f.read())
        f.close()
