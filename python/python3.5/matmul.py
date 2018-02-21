r1=eval(input("enter no.of rows"))
c1=eval(input("Enter no.of columns"))
r2=eval(input("enter no.of rows"))
c2=eval(input("enter no.of columns"))
if (c1!=r2):
	print("enter the coumns of 1st matrix and rows of 2nd matrix equal")
	c1=eval(input("Enter no.of columns"))
	r2=eval(input("enter no.of rows"))
lst1=[[eval(input()) for x in range(c1)] for y in range(r1)]
#print(lst)
lst2=[[eval(input()) for x in range(c2)] for y in range(r2)]
lst3=[[int(0) for x in range(c2)] for y in range(r1)]
for x in range(r1):
	for y in range(c2):
		for z in range(c1):
			lst3[x][y]+=lst1[x][z]*lst2[z][y]
for x in range(r1):
	for y in range(c2):
		print(lst3[x][y])
		