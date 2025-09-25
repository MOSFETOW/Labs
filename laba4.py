def format_price(price: float) -> str:
    #Форматує ціну у вигляді 'ціна: xxx.xx грн
    rounded = round(price, 2)  
    price_str = str(rounded)
    if "." not in price_str:
        price_str += ".00"
    else:
        whole, decimal = price_str.split(".")
        decimal = (decimal + "0")[:2]
        price_str = f"{whole}.{decimal}"
    return f"ціна: {price_str} грн"


store_items = [
    {"назва": "хліб", "наявність": True, "ціна": 13},
    {"назва": "молоко", "наявність": True, "ціна": 123},
    {"назва": "яйця", "наявність": True, "ціна": 17},
    {"назва": "цукор", "наявність": True, "ціна": 56},
    {"назва": "сіль", "наявність": False, "ціна": 97},
    {"назва": "масло", "наявність": False, "ціна": 12.50},
    {"назва": "сир", "наявність": True, "ціна": 89},
    {"назва": "ковбаса", "наявність": True, "ціна": 54},
    {"назва": "борошно", "наявність": True, "ціна": 76.09},
    {"назва": "чай", "наявність": True, "ціна": 123},
]



#Перевіряє наявність  товарів у магазині
def check_availability(*products):
    global store_items
    
    result = {}
    for product in products:
        if product in store_items:
            result[product] = True
        else:
            result[product] = False
    return result


# Приклад використання
print(format_price(123.4))
print(format_price(1.467))
print(format_price(353))  


print(check_availability("хліб", "яблука", "чай"))




def market(command: str):
    parts = command.split()
    action = parts[0]   # "купити" або "ціна"
    products = parts[1:]  # список товарів
    
    if action == "купити":
        not_available = []
        i = 0
        while i < len(products):
            product = products[i]
            found = False
            j = 0
            while j < len(store_items):
                item = store_items[j]
                if item["назва"] == product and item["наявність"]:
                    found = True
                    break
                j += 1
            if not found:
                not_available.append(product)
            i += 1
        
        if len(not_available) > 0:
            print("Купівля не відбулась!")
            k = 0
            while k < len(not_available):
                if k == 0:
                    print(not_available[k], end="")
                else:
                    print(", " + not_available[k], end="")
                k += 1
            print(" - немає в наявності")
        else:
            print("Куплено: ", end="")
            i = 0
            while i < len(products):
                if i == 0:
                    print(products[i], end="")
                else:
                    print(", " + products[i], end="")
                i += 1
            print()
    
    elif action == "ціна":
        i = 0
        while i < len(products):
            product = products[i]
            j = 0
            found = False
            while j < len(store_items):
                item = store_items[j]
                if item["назва"] == product:
                    print(f"{product} ціна: {item['ціна']} грн")
                    found = True
                    break
                j += 1
            if not found:
                print(f"{product} - немає такого товару")
            i += 1


# Приклади роботи:
market("купити молоко цукор сіль")
# Купівля не відбулась!
# сіль - немає в наявності

market("купити сіль цукор масло")
# Купівля не відбулась!
# сіль, масло - немає в наявності

market("купити молоко цукор чай")
# Куплено: молоко, цукор, чай

market("ціна молоко цукор сіль")
# молоко ціна: 123 грн
# цукор ціна: 56 грн
# сіль ціна: 97 грн
    
    





