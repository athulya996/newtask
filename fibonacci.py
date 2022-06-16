# Python Program to Print the Fibonacci sequence.
num = int(input("how many numbers? : "))
n1, n2 = 0, 1
count = 0
if num <= 0:
    print("please enter a positive integer : ")
elif num == 1:
    print("Fibonacci sequence upto ",num, ":")
    print(n1)
else:
    print("Fibonacci sequence :")
    while count < num:
        print(n1)
        n = n1+n2
        n1 = n2
        n2 = n
        count += 1