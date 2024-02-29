

""" 
if x%11 == 0 and y%11 == 0 
     print("gcf is 11")


     if x%10 == 0 and y%10 == 0 
     print("gcf is 10")


      if x%9 == 0 and y%9 == 0 
     print("gcf is 9")


      if x%8 == 0 and y%8 == 0 
     print("gcf is 8")


      if x%7 == 0 and y%7 == 0 
     print("gcf is 7")

      if x%3 == 0 and y%3 == 0 
     print("gcf is 3")


      if x%2 == 0 and y%2 == 0 
     print("gcf is 2")
 """

number1 = int(input("choose a number"))
number2 = int(input("choose another number"))

list1 = []
number = 1
def factor():
 if number1 > number2:
    number = number1
 elif number1 < number2:
    number = number2

 for i in range (1, number+1):
    if number1 % i == 0 and number2 % i == 0:
     list1.append(i)
    print(max(list1))
factor()