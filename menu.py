# make as dictionary as Menu and Display Function

menu = {
    1:{'name':'Burger','price':500},
    2:{'name':'Potato','price':300},
    3:{'name':'Coffee','price':200},
}

def display_menu():
    print('This is Menu')
    for ID,Item in menu.items():
        print(f"{ID} : {Item['name']} - {Item['price']}$")
        
display_menu()