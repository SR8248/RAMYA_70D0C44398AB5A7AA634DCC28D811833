

def linearSearchProduct(productList,targetproduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetproduct:
      indices.append(index)

  return indices


#Example usage
products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
result = linearSearchProduct(products, target)
print(result)
