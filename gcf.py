

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

x = input("choose a number")
y = input("choose another number")

def factors(gcf):
    factorlist = []
    for i range (1, gcf+1):
        if gcf%i == 0 
        factor list 