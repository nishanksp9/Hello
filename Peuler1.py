x= int(input("Enter a number:"))
sumtn=0
i=0
while i<x:
    if i%3==0 or i%5==0:
        sumtn += i
    i += 1
print("The sum is:", sumtn)
        