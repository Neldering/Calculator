def computepay(hours,rate) :
	if hours <= 40 :
		pay = rate * hours
	else :
		pay = rate * 40 + ( rate * 1.5 * ( hours - 40) ) # assumes past 40 hours is overtime and uses this formula
	return pay
	

inp = raw_input("Please Enter Hours: ")
hours = float(inp)
inp = raw_input("Please Enter Rate: ")
rate = float(inp)

pay = computepay(hours,rate)
print pay
