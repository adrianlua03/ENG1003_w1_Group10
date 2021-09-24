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
  while(i < side):
    j = 0
    while(j < side):      
        j = j + 1
        print('[]', end = '  ')
    i = i + 1
    print('')
    
