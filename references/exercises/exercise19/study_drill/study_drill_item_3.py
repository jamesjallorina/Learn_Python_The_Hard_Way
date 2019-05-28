#!/usr/bin/python

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# my function
def function_template(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    print(f"adding two arguments: {arg1 + arg2}")

print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50


cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too: ")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variable and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# using my function in 10 ways

function_template("does it add ", "strings?")
function_template("yes strings ", "can be added")
function_template("does it add ", "two integers?")
function_template(5, 10)
function_template("yes two integers ", "can be added")
function_template("does it add ", "two floats?")
function_template(10.5, 10.5)
function_template("yes two floats ", "can be added")
function_template("Let's add ", "two doubles")
function_template(20.50, 30.90)
