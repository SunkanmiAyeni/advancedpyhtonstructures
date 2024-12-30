sca=(1,8,9,5)
vas=(1,2,9,4)
asd=list(zip(sca,vas))
print(asd)
reverse=list(zip(sca,vas[::-1]))
print(reverse)
myDict={x:y for x,y in zip(sca,vas)}
print(myDict)