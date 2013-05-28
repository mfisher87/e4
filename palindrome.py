#! /usr/bin/env python3.3

def isPalindromic(i):
	if int(str(i)[::-1]) == i: return True

palindromicProduct = 0

for var1 in range(100,999):
	for var2 in range(100,999):
		product = var1 * var2
		if product > palindromicProduct and isPalindromic(product): 
			palindromicProduct = product
			print(palindromicProduct)

print("Hooray!",palindromicProduct)
