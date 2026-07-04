base_price = 15
age = int(input('Enter your age: '))
seat_type = input('Enter seat type (Premium/Gold/Regular): ')
show_time = input('Enter show time (Morning/Evening): ')

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = input('Are you a member? (yes/no): ')
is_weekend = input('Is it a weekend? (yes/no): ')
discount = 0
if is_member == 'yes' and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend == 'yes' or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member == 'yes'):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    final_price = base_price + extra_charges + service_charges - discount
    print("Final price of ticket:", final_price)   
else:
    print('Ticket booking failed due to restrictions')