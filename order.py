from menu import menu

# Define a Function to take orders 
def take_order():
    '''The Function of taking order'''
    order = []
    total = 0
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
    return order, total