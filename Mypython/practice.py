def add(x, y):
    sum_result = x + y
    print(sum_result)
    return sum_result

def multiply(a,b):
    product_result = a * b
    print(product_result)
    return product_result

def print_result(result):
    print("The result is:", result) 


value1 = 5
value2 = 10



sum_result = add(value1, value2)
product_result = multiply(value1, value2)
total_result = add(sum_result, product_result)

print_result(total_result)
