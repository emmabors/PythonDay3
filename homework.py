#Excercise 1:
grocery_cart = []
prompt = "\nWhat would you like to add or delete to the grocery cart: (if deleting, enter 'delete' first then the item)"
prompt += "\nEnter 'quit' to finish list."
prompt2 = "What would you like to delete?"
message = " " 
while message != 'quit':
    message = input(prompt)
    print(message)
    grocery_cart.append(message)
    print(grocery_cart)
    if message == 'delete':
        message2 = input(prompt2)
        grocery_cart.remove(message2)
        grocery_cart.remove('delete')
grocery_cart.remove('quit')
print('Here is your final list:')
print(grocery_cart)


#Excercise 2:
import mathmodule

print(mathmodule.multiply_nums(5, 10))

print(mathmodule.circumference(6, 3.141592653589793))
