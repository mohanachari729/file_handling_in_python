# #value error
# try:
#     num1 = int(input("enter the first number:"))
#     num2 = int(input("enter the second number :"))
#     print(num1 + num2)
#     print(num1 - num2)
#     print(num1 * num2)
# except ValueError as e:
#     print(f"error occured {e}")
# else :
#     print(num1 ** num2)
# finally :
#     print("this is perform mathamatical operations")

# ##type error
# try:
#    num1 = '10'
#    num2 = 20
#    result = num1/num2
#    print(result)
# except TypeError as e :
#     print(f"it's has a error occured {e}")
# finally :
#     print("num1 taken as string")


# #zeroDivision Error
# try:
#     num1 = 10
#     num2 = 0
#     print(num1 * num2)
#     print(num1 / num2)
# except ZeroDivisionError as e:
#     print(f"ZeroDivisionError: {e}")
# else :
#     print(num1 + num2)
#     print(num1 - num2)
# finally :
#     print(" denominator value is 0 ")


# ##file not found error
# try:
#     file = open("mohan.txt",mode = 'r')
#     read_file = file.read()
#     print(file)
#     file.close()
# except FileNotFoundError  as e:
#     print(f"hey! this file will be not found {e}")
# finally:
#     print("create a file using another mode")

# ## Index error
# try:
#     list1 = [1,2,3,4]
#     print(list1[2])
#     print(list1[4])
# except IndexError as  e:
#     print(f"enter the correct index value {e}")

# ### key error
# try:
#     dict_1 = {'username':'mohan'}
#     print(dict_1['usernames'])
# except KeyError as e :
#     print(f"enter the currect key {e}")
# else :
#     print(dict_1)
# finally :
#     print("this is the final block")

# ## attribute error
# try:
#     string = "hello pythonlife"
#     print(string.reverse())
# except AttributeError as e :
#     print(f"there is error occured {e}")
# finally:
#     print("unsopported attribute can be used")

# ##overFlow error
# try:
#     num = 5000.456
#     for i in range(1,1000):
#         n =  num**i 
#         print(n)
# except OverflowError as e:
#     print(f"over flow error can be occured ")
# finally:
#     print("enter the limited range")

# # I/O error
# try:
#     file = open("sample.txt",mode='w')
#     file.write("my name is mohanachari")
#     print(file.read())
# except IOError as e :
#     print(f"input and output error can be occured {e}")
# finally :
#     print("check the code ")


##Exception
balance = 500
def display_menu():
    print("\ATM MENU:")
    print("1.CREDIT")
    print("2.DEBIT")
    print("3.balance")
    print("4.EXIT")
def get_choice():
    return input("enter your option(1-4):")
def CREDIT():
    try:
        global balance
        amount = float(input("enter your amount:"))
        if amount <= 0 :
            print("enter the positive amount")
        else :
            balance += amount
            print(f"${amount}credited in your account")
            print(f"you total balance is ${balance}")
    except Exception as e :
        print(f"please enter the numericals {e}")
def DEBIT():
    try:
        global balance
        amount = float(input("enter your amount:"))
        if amount > balance :
            print("your account have a not sufficient balance")
        else :
            balance -= amount
            print(f"the ${amount} has been debited in your account")
            print(f"your total balance is ${balance}")
    except Exception as e :
        print(f"enter the numericals {e}")
def show_balance():
    print(f"your total balance is ${balance}")
def main():
    while True :
        display_menu()
        choice=get_choice()
        if choice == "1":
            CREDIT()
        elif choice == "2":
            DEBIT()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            print("thank for using ATM have a nice day")
            break
        else :
            print("please enter the valid choice")
main()

