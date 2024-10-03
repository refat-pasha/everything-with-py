def bookstore():
    num_of_books = int(input("enter the number of books"))
    while num_of_books <= 0:
        print("Number of books cannot be zero or negative")
        num_of_books = int(input("Please enter a valid number of books: "))

    total_cost = 0
    for i in range(1, num_of_books+1):
        price = float(input(f"Price of books {i}: "))
        while price<0:
            print("Price cannot be negative")
            price = float(input(f"Please enter a valid price for book {i}: "))

        total_cost += price
    if 1<= num_of_books <=3:
        discount = 0
        discount_persentage = 0
    elif 4<= num_of_books <=10:
        discount_persentage = 10
        discount = total_cost * (discount_persentage/100)
    else:
        discount_persentage = 20
        discount = total_cost *(discount_persentage/100)
    payable_cost = total_cost - discount
    print(f"Total Cost: {total_cost:.2f}tk")
    if discount > 0:
        print(f"Total Payable Cost: {payable_cost:.2f}tk ({discount_persentage}% discount applied for purchasing {num_of_books} books")
    else:
        print(f"Total Payable Cost: {payable_cost:.2f}tk (No discount applied)")
bookstore()