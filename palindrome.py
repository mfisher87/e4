#! /usr/bin/env python3.3

def isPalindromic(i):
	if int(str(i)[::-1]) == i:
		return True

maxPalindromicProduct = 0

for var1 in range(100,999):
	for var2 in range(100,999):
		product = var1 * var2
		if isPalindromic(product):
			palindromicProduct = product
			if palindromicProduct > maxPalindromicProduct: 
				maxPalindromicProduct = palindromicProduct
				print(palindromicProduct)

print("Hooray!",maxPalindromicProduct)
