a1=int(input ("enter 1st number"))
a2=int(input ("enter 2nd number"))
a3=int(input ("enter 3rd number"))
a4=int(input ("enter 4th number"))
a5=int(input ("enter 5th number"))
if a1>a2 and a1>a3 and a1>a4 and a1>a5:
	print("a1 is greater")
elif a2>a3 and a2>a4 and a2>a5:
	 print("a2 is greater")
elif a3>a4 and a3>a5:
	 print("a3 is greater")
elif a4>a5:
	print("a4 is greater")
else:
    print("a5 is greater")