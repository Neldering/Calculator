def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def multi(x,y):
	return x*y
	
def div(x,y):
	return x/y
	
print("Select Operand")
print("1. Add")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter Choice(1/2/3/4):"))
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


if choice == 1:
	print(x,'+',y,'equals',add(x,y))
elif choice == 2:
	print(x,"-",y,"equals",sub(x,y))
elif choice == 3:
	print(x,"*",y,"equals",multi(x,y))
elif choice == 4:
	print(x,"/",y,"equals",div(x,y))
else:
	print("Invalid number")
