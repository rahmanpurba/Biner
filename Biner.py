#!/usr/local/bin/python3.7

import random

import string

stack = ''.join([random.choice(string.ascii_lowercase) for j in range(100)])

rdi = ""

rsi = ""

rdx = "0"

def get_file():

	print(open(rdi, rsi).read()[:int(rdx)])

def popstack():

	global stack

	ret_val = stack[:8].strip()

	stack = stack[8:]

	return ret_val

def gadget_1():

	global rdi

	rdi = popstack()

	return_address = popstack()

	globals()[return_address]()

def gadget_2():

	global rsi

	rsi = popstack()

	return_address = popstack()

	globals()[return_address]()

def gadget_3():

	global rdx

	rdx = popstack()

	return_address = popstack()

	globals()[return_address]()

def gadget_4():

	print("test")

def vuln():

	global stack

	buf = input().ljust(32, ' ')

	stack = buf[:56] + stack

	print(buf)

	stack = stack[32:]

	return_address = popstack()

	globals()[return_address]()

def main():

	global stack

	print("Good Luck~")

	stack = "main_end".ljust(8, ' ') + stack

	vuln()

def main_end():

	print("Thank you~")

if __name__ == '__main__':

	main()
