with open("test2.txt", "w") as test2:
	test2.write("some text")
with open("test2.txt", "a") as test2:
	test2.write("\nEven more text")
with open("test2.txt") as test2:
	readvar = test2.read()
print(readvar)