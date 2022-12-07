menu = {
    'ramen': {'noodles', 'egg', 'pepper'},
    'beshbarmak': {'noodles', 'onion', 'meat'},
    'manty': {'dough', 'onion', 'meat', 'potato'},
    'makarons': {'pasta', 'potato', 'meat'},
    'plov': {'rice', 'carrot', 'butter'},
    'pizza': {'dough', 'sausage', 'chees'},
    'burger': {'bread', 'cutlet', 'tomato', 'cucumber'}
}


while True:
    user_input = input('введите продукт: ')
    for name, ingrs in menu.items():
        if user_input in ingrs:
            print(name)