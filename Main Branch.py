start = input("Enter the function to be executed: ")
if start == "1":
    x = int(input("Height:"))

    print("xxx\n"*x)
elif start == "2":
    #Jay's function
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

    
# LT visited here :)

