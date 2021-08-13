sub1=int(input("Enter marks of the 1st subject  1"))
sub2=int(input("Enter marks of the 2nd subject  2"))
sub3=int(input("Enter marks of the 3rd subject"))
sub4=int(input("Enter marks of the 4th subject"))
sub5=int(input("Enter marks of the 5th subject"))

total=sub1+sub2+sub3+sub4+sub5
# new change by remote
print("Total marks is:", total )
avg=(sub1+sub2+sub3+sub4+sub5)/5
# test tst
if avg>=80 and avg<=100:
	print("Grade:A")
else:
	if avg>=60 and avg<=79:
		print("Grade:B")
	else:
		if avg>=40 and avg<=59:
			print("Grade:C")
		else:
			if avg>=20 and avg<=39:
				print("Grade:D")
			else:
					print("Grade:E")


percentage=(total/500)*100
print("Percentage is", percentage)
if percentage>33:
	print("Result is: Pass")
#new change my local
else:
		print("Result is: Fail")
