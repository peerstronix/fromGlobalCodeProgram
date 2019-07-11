
def printStars(n):
	for i in range(0, n):
		for j in range(0, i+1):
			print("* ", end=" ")
		print("\r")



n = int(input("What  will be the maximum number of stars on a line?"))

printStars(n)
