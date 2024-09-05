from calc_func import calculate

def get_input() :
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    return num1, num2, operator

def main():
    num1, num2, operator = get_input()
    result = calculate(num1, num2, operator)
    print(f"The result of {num1} {operator} {num2} is: {result}")
   
main()