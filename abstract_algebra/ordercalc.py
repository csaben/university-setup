# Calculating the orders of elements in Z_7* under multiplication modulo 7

# The elements of Z_7*
elements = [1, 2, 3, 4, 5, 6]

# Function to find the order of an element in Z_7*
def order_in_Z7_star(element):
    n = 1
    while pow(element, n, 7) != 1:
        n += 1
    return n

# Calculating the orders of each element
orders = {element: order_in_Z7_star(element) for element in elements}
print(orders)
print(len(orders))

