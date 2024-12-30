number1=[1,2,4,5]
number2=[3,4,9,6]
sum=map(lambda a,b:a+b,number1,number2)
print("The list containing all of the numbers is",list(sum))
numbers=[1,5,7,3]
def square(n):
    return n*n
sq=list(map(square,numbers))
print("The squared list is sq",sq)