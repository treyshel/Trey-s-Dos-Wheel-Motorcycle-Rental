# call the inventory.txt file in my parameter when I run this function
def dos_inventory():
    ''' None -> [str, [str, str, float, int]]
    [[0660, '2006 Suzuki GSXR 600', 'blue', 3499.99, 5], [0410, '2004 Yamaha R1 1000', 'red', 3749.99, 9], [0190, '2001 Kawasaki Ninja ZX-9R 900', 'grey', 2995.99, 4], [1650, '2016 Honda CBR 500', 'white', 6499.99, 2], [1765, '2017 Kawasaki Ninja EX 650', 'green', 7499.99, 4], [0910, '2009 Suzuki GSX 1000 Hayabusa', 'black', 7299.99, 8]]
    '''
    with open('inventory.txt', 'r') as file:
        l = file.readline().strip().split(', ')
        lines = file.readlines()
    return [l, lines]


def store_revenue_helper():
    ''' [[str ,str, str]] -> None'''
    history = []
    with open('history.txt', 'r') as documented_rentals:
        documented_rentals.readline()
        read_rest = documented_rentals.readlines()
    for lines in read_rest:
        split = lines.strip().split(', ')
        history.append(
            [str(split[0]),
             str(split[1]),
             float(split[2].replace('$', ''))])
    return history


def store_revenue():
    price = 0
    history = store_revenue_helper()
    for item in history:
        item[2] = float(item[2]) + float(item[2])
        price += item[2]
    return price


def in_history(type_of_motorcycle, days, total):
    with open('history.txt', 'a') as history:
        history.write(
            '\n{}, {}, ${:.2f}'.format(type_of_motorcycle, days, total))


def quantity_take_away(inventory, type_of_motorcycle):
    ''' item, string, int, -> None '''
    key1, key2, key3, key4, key5 = 'code', 'type_of_motorcycle', 'color', 'price', 'quantity'
    new_quantity = '{}, {}, {}, {}, {}'.format(key1, key2, key3, key4, key5)
    inventory[type_of_motorcycle]['quantity'] -= 1
    for items in inventory.values():
        new_quantity += '\n{}, {}, {}, {}, {}'.format(
            items.get(key1),
            items.get(key2), items.get(key3), items.get(key4), items.get(key5))
    with open('inventory.txt', 'w') as file:
        return file.write(new_quantity)


#exact same as take away just add 1 instead of subtract
def quantity_after_return(inventory, type_of_motorcycle):
    ''' item, string, int -> None'''
    key1, key2, key3, key4, key5 = 'code', 'type_of_motorcycle', 'color', 'price', 'quantity'
    new_quantity = '{}, {}, {}, {}, {}'.format(key1, key2, key3, key4, key5)
    inventory[type_of_motorcycle]['quantity'] += 1
    for items in inventory.values():
        new_quantity += '\n{}, {}, {}, {}, {}'.format(
            items.get(key1),
            items.get(key2), items.get(key3), items.get(key4), items.get(key5))
    with open('inventory.txt', 'w') as file:
        return file.write(new_quantity)


def history_for_return(type_of_motorcycle, days, total_of_deposit_return):
    with open('history.txt', 'a') as history:
        history.write('\n{}, {}, $-{}'.format(type_of_motorcycle, days,
                                              total_of_deposit_return))
