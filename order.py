from menu import menu

# Define a Function to take orders 
def take_order():
    '''The Function of taking order'''
    order = [] # The List to store the food be ordered
    total = 0 # The variable to calculate the money
    while True:
        choice = input("Enter the number of the food you want(finish by enter 0):")
        if choice == '0':
            break
        elif int(choice) in menu:
            order.append(menu[int(choice)]) #辞書の要素の特定方法
            total += menu[int(choice)]["price"]
            print(f"{menu[int(choice)]['name']}を追加しました。")
        else:
            print('無効な番号です。')
    return order, total # The return value can be two