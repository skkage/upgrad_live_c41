from summation import sum_
from multiplication import mult

if __name__ == "__main__":
    x = int(input("Enter a integer"))
    y = int(input("Enter a integer"))
    print(f"Summation of x: {x} and y: {y} is: {sum_(x,y)}" )
    print(f"Multiplication of x: {x} and y: {y} is: {mult(x,y)}" )
    

