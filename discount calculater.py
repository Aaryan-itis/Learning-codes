def apply_discount(price, discount):

    if not isinstance(price, (int, float)):
        print("The price should be a number")
    if not isinstance(discount, (int, float)):
        print("The discount should be a number")
    if price <= 0 :
        print("The price should be greater than 0")
    if discount < 0 or discount > 100 :
        print("The discount should be between 0 and 100")
    else :
        calc = (discount * price)/100
        final_price = price-calc
        print(final_price)

x = float(input("Enter the price: "))
y = float(input("Enter the discount: "))
apply_discount(x, y)