"""
    title: Franks_Factorial_Factory.py
    written by: Jessica Soler
    Date: 9/26/2024
    purpose: using while/for loop to calculate factorial
"""
#import rich console
from rich.console import Console
console = Console()

DASHES = "-" * 55

# In mathematics, the factorial is the product of all positive whole numbers less than or equal to a target number. 

# In a math equation, factorial is denoted with an exclamation mark. 

# For example: 5! = 5 x 4 x 3 x 2 x 1 = 120

# This program will iterate the value from start to end using a for loop.

# For every number, multiply by the last product and accumulate the result.

def main():
    
    # print a rich title
    console.print(DASHES, style="bold blue")
    console.print("\tWelcome to Frank's Factorial Factory", style="bold red")
    console.print(DASHES, style="bold blue")
    
    get_factorial()


def get_factorial():
    
    factorial = int(input("Enter a positive, whole number: "))
    

    # set the accumulator to 1
    accumulator = 1
        
    # iterate from 1 to the target number
    for i in range(1, factorial + 1):
        accumulator *= i
            
    console.print(f"The factorial of {factorial} is {accumulator}.")
    play_again()
    
def play_again(): 
    # ask user if they want to continue
    response = input("Would you like to continue? (y/n): ")
       
    if response.lower() == "y":
        get_factorial()
    else:
        console.print("Goodbye!")
        exit()


        
        
main()