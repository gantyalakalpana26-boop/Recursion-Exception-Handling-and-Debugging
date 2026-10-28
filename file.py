# 1. Recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial : ",factorial(5))

#2. Exception Handling
try:
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))

    result=num1/num2

    print("Result",result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid number")

finally:
    print("Program Completed")

# 3. Debugging
def add_numbers(a,b):
    res=a+b
    return res
res=add_numbers(550,20)
print("Sum:", res)