products = [10,14,22,33,44,13,22,55,66,77]
cart = []
totalsum = 0

def checkout(total):
    for i in cart:
        total += i
    print("Total", total)
    payment = int(input("Payment: "))
    if payment > total:
        print("Change: ", payment - total)

def add_product(pos):
    index = pos - 1
    cart.append(products[index])
    print(f"Product:  {pos} Price:  {products[index]}")

def main():
    print("Supermarket")
    print("===========")
    while True:
        selection = int(input("Please select product (1-10) 0 to Quit: "))
        if selection == 0:
            checkout(totalsum)
            break
        else:
           add_product(selection)
    return 0
if __name__ == "__main__":
    main()