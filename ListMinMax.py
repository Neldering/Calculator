#not really a calculator but it's in here
largest = None
smallest = None
the_list = []
while True:
	num = raw_input("Enter a number: ")
	if num == "done": break
	try:
		number = int(num)
		the_list.append(number)
	except:
		print 'Invalid input'
for value in the_list:
	if smallest is None:
		smallest = value
	elif value < smallest:
		smallest = value
for list_num in the_list:
	if largest is None:
		largest = list_num
	elif list_num > largest:
		largest = list_num
print "Maximum is", largest
print "Minimum is", smallest
