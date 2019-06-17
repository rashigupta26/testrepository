#check if a number is prime or not
a=int(input("enter any  number "))
if a>1:
	for i in range(2,a):
		if (a%i)==0 :
			print(a,"is not prime")
		else:
		    print(a,"is a prime")
else:
    print(a,"is not a prime number")			