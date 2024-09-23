def place_order(
        customer_name,
        price,
        quantity,
        discount = 0,
        shipping_fee = 10):
    total_price = (price * quantity) - discount + shipping_fee
    if total_price > 1000:
        discount = .1
        cal_discount = total_price * discount
        return f"{customer_name} have %discount: {cal_discount} \nand total price is: {total_price-cal_discount}"
    else:
        return f"{customer_name} have total price: {total_price}"
print(place_order("refat", price=10, quantity=10))
print(place_order("pasha", price=1000, quantity=55))