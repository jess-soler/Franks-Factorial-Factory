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
    
    factorial = input("Enter a positive, whole number: ")
    
    if factorial == str:
        console.print("Factorial must be a whole, positive number", style="bold red")
    # factorial needs to be a positive number
    elif factorial == int<0:
        console.print("Factorial must be a whole, positive number", style="bold red")
    # factorial needs to be a whole number
    elif factorial == float:
        console.print("Factorial must be a whole, positive number", style="bold red")
    # factorial cannot be a string


        
        
main()