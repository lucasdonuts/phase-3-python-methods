#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2

# function greet_programmer() prints "Hello, programmer!" F
# function greet() prints "Hello, {name}!" F
# function greet_with_default() prints "Hello, programmer!" F
# function greet_with_default() prints "Hello, {name}!" F
# function add() calculates 45 + 55 = 100 F
# function halve() halves integer input F
# function halve() halves float input F