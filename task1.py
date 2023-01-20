
"""
Custom hashing function tweakable to any data.
No collision handling techniques are used here.
"""
def hashString(string):
  base = 3
  mod = 997
  hash_val = 0

  for i in range(len(string)):
    hash_val = (hash_val + (ord(string[i]) * (base**i % mod) % mod))  % mod

  return hash_val

"""
Compares sold items prices to reference values.
"""
def priceCheck(products, productPrices, productSold, soldPrice):
  counter = 0
  refPrices = [0] * 1000
  
  for i in range(len(products)):
    refPrices[hashString(products[i])] = productPrices[i]

  for j in range(len(productSold)):
    if soldPrice[j] != refPrices[hashString(productSold[j])]:
      counter += 1
  
  return counter

def main():
  print(priceCheck(
  	products=['rice', 'sugar', 'wheat', 'cheese'],
  	productPrices=[16.89, 56.92, 20.89, 345.99],
  	productSold=['rice', 'cheese'],
  	soldPrice=[18.99, 400.89]
  ))

if __name__ == '__main__':
  main()


  