start = input("Enter the function to be executed: ")
if start == "1":
  x = int(input("Height:"))
  while x>0:
      print("xxx")
      x-=1
elif start == "2":
  a = int(input("First Number: "))
  b = int(input("Second Number: "))
  s = a + b
  print("The sum is: ", s) 
elif start == "3":
  x = int(input("List Length:"))
  while x>0:
    print(x)
    x-=1
elif start == "4":
  side = int(input("Please Enter the Sides of a Square  : "))
  i = 0
  print("Square Size: ", side)

  while(i < side):
      j = 0
      while(j < side):      
          j = j + 1
          print('[]', end = '  ')
      i = i + 1
      print('')

elif start == "5":
  import random

  r = random.randint(50,200)
  x = random.randint(1,r)
  y=0
  z=1
  print('The range for this round is 1 -', r)
  t = 0

  while not y == x:
      y = int(input("Make a guess:"))
      if y>x:
          r=y
          print('The range is now',z,'-',r,'\n')
          t+=1
      
      elif y<x:
          z=y
          print('The range is now',z,'-',r,'\n')
          t+=1

      else:
          t+=1
          print('BINGO! You took',t,'attempts to reach the answer!','\n')
# LT visited here :)



