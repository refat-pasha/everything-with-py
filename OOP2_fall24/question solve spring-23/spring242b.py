def bookstore(num_of_books):
    total_cost = sum(num_of_books)
    if len(num_of_books) <= 3:
        discount = 0
    elif 4 <= len(num_of_books) <= 10:
        discount = .10
    else:
        discount = .20
    total_payable = total_cost - (total_cost*discount)
    return total_cost , total_payable , discount
n = int(input("Enter the number of books: "))
num_of_books = []
for i in range(n):
    price = int(input(f"Price of book-{i}: "))
    num_of_books.append(price)
total_cost, total_payable, discount = bookstore(num_of_books)
print(f"Total Cost: {total_cost}tk")
#print(f"Total Payable Cost {total_payable}tk")
if discount > 0:
    print(f"Total Payable Cost {total_payable}tk ({int(discount * 100)}% discount applied for purchasing {len(num_of_books)} books)")
else:
    print(f"Total Payable Cost {total_payable}tk (No discount applied)")

