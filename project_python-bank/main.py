import itertools as it
from Acount import Acount
from privateAcount import privateAcount
flag=0
index=0
users={8000:{'name':"racheli","sum":45},8001:{'name':"esti","sum":99},8002:{'name':"etty","sum":40},8003:{'name':"shmuel","sum":-855}}

def endlessNumbers():
    for j in it.count():
        yield j
def update_mony():
    """update the sumMonyInAcount in dict"""
    users[index-1][private.namePerson]=private.sumMonyInAcount
def addUser():
    global index
    """add user to the dict"""
    users[index]={"name":private.namePerson,'sum':private.sumMonyInAcount}
    index += 1
def positiv():
    usersDebitBalance=list(filter(lambda x: x['sum']>0,users.values()))
    print(usersDebitBalance)
default_value=endlessNumbers()
try:
    newAcount = int(input("ליצירת חשבון חדש הקש 1 אחרת 0"))
except:
    newAcount=0
    print("אופס משהו השתבש החל שוב בהרצה")
if newAcount == 1:
    x = 0
    y = 0
    z = "null"
    w = 0
    try:
        x = int(input("הכנס מספר חשבון"))
    except:
        x = next(default_value)
        print(f"מספר חשבון ברירת מחדל הוא: {x}")
    try:
        y = int(input("הכנס את הסכום הראשוני"))
    except:
        y = 0
    try:
        z = input("הכנס שם")
    except:
        z = "null"
    try:
        w = int(input("הכנס סכום לחריגה"))
    except:
        w = 0
    private = privateAcount(x, y, z, w)
    addUser()

def func1():
    try:
        sum = int(input("הכנס סכום למשיכה"))
        private.cash_withrawal(sum)
        update_mony()
    except:
        print("הוכנס קלט לא תקין")
def func2():
    try:
        sum = int(input("הכנס סכום להפקדה"))
        if(sum<0):
            raise ValueError
        private.Deposit_money(sum)
        update_mony()
    except ValueError:
        print("אי אפשר להכניס סכום נמוך מ0")
    except:
        print("הוכנס קלט לא תקין")

def func3():
    private.Account_Balance()
def func4():
    private.View_recent_actions()

while newAcount==1 and flag==0:
    try:

        print("בכל שלב:")
        print("למשיכת כסף מחשבונך הקש 1")
        print("להפקדת כסף הקש 2")
        print("לצפיה ביתרה הקש 3")
        print("לצפיה בפעולות אחרונות הקש 4")
        num=int(input())
        if num==1:
            func1()
        elif num==2:
            func2()
        elif num==3:
            func3()
        else:
            func4()
    except:
        print("אפשרות בחירה לא קיימת בתפריט תודה")
    flag=int(input("ליציאה הקש 1 אחרת הקש 0"))
    print(flag)
print("כל האנשים שלא בחובות:")
positiv()
if newAcount == 0:
    print("אי אפשר לעשות פעולות בחשבון בלי להתחבר")





























