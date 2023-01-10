print('''
    Choose Your option
    1. function 1
    2. function 2
    3  exit

    ''')

input_value = int(input("Choose No. :-  "))

def fun1():
    print("1 press")

def fun2():
    print("2 press") 
    
def fun3():
    exit


if input_value == 1:
    fun1()
elif input_value == 2:
    fun2()
else:
    fun3()




