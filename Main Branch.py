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
  un = random.randint(1, 200)
  x = 0

  while not x == un:
      x = int(input("Guess: "))
      if x<un:
          print("Too low")
      elif x>un:
          print("Too high")
      else:
          print("Correct")

# LT visited here :)



