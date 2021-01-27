# def thing(name. age=82, *args, **kwargs thing: 'something'):  # kwargs come ack  as a Dictionary.
#     pass


# def person(**kwargs):
#     print(kwargs)  # {'name': 'Sandra', 'age': 81, 'brain': 'Huge'}
#     print(type(kwargs))  # <class 'dict'>

#     if 'age' in kwargs:
#         print("Your age is ", kwargs.get("age"))  # Your age is  81

# person(name="Sandra", age=81, brain="Huge")



def order_pizza(name, address, **toppings):
    print(f"Order is for {name}")  # Order is for Amanda
    print(f"Ship it to {address}")  # Ship it to Canada
    price = 18.00
    for key, value in toppings.items():
        price = price + 2.00
    print(f"The total price is {price}")  # 
    return price

total_price = order_pizza("Amanda", "Canada", jalapenos=True, extra_cheese=True, ham=True)

