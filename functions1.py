def bill(amount,tip):
    total =amount*(1+0.01*tip)
    print("Please pay:",round(total,2))
bill(50,20)
def cube(number):
    return (number**3)
def divisibility(number):
    if number%3==0:
        return (cube(number))
    else:
        return (False)
print(divisibility(20))
print(divisibility(9))
def factorial(x):
    if x==0 or x==1:
        return (1)
    else:
        return(x*factorial(x-1))
print (factorial(3))

