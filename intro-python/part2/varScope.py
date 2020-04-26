#!/usr/bin/env python

#Module Variables

module_variable="module_variable"

def myFunc(argument_variable):
		local_variable="local_variable"
		print("I am",module_variable,".. I am visibile module-wide..")
		print("I am",argument_variable,".. I can be passed into function..")
		print("I am",local_variable,".. I can only be accessed inside the function..")

myFunc(argument_variable="argument_variable")

print("Trying to access local_variable outside of function. . .")

try:
	print(local_variable)

except NameError as error:
	print(error)

