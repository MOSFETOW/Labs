

def format_price(price: float):
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






store_items = [
    {"хліб": True, "ціна": 13},
    {"молоко": True, "ціна": 123},
    {"яйця": True, "ціна": 17},
    {"цукор": True, "ціна": 56},
    {"сіль": False, "ціна": 97},
    {"масло": False, "ціна": 12.50},
    {"сир": True, "ціна": 89},
    {"ковбаса": True, "ціна": 54},
    {"борошно": True, "ціна": 76.09},
    {"чай": True, "ціна": 123}
]

def order(*args, buy=False):
    total = 0
    available = True

    # Перевіряємо наявність кожного товару
    for product in args:
        found = False
        for item in store_items:
            if product in item:
                found = True
                if item[product]:  # якщо товар є в наявності
                    total += item["ціна"]
                else:
                    print(f"Товар '{product}' відсутній .")
                    available = False
                break

        if not found:
            print(f"Товар '{product}' не знайдено ")
            available = False

    # Якщо користувач лише переглядає ціну
    if not buy:
        print(f"Загальна вартість вибраних товарів: {total} грн.")
        return

    # Якщо користувач хоче купити
    if buy and available:
        print(f"Замовлення прийнято! {total} грн.")
    else:
        print("Замовлення неможливе, бо товари відсутні.")

def main():



    # Приклад використання
    print(format_price(123.4))
    print(format_price(1.467))
    print(format_price(353))  
    
    
    print(check_availability("хліб", "яблука", "чай"))




    
    # приклади використання:
    order("молоко", "чай", buy=False)   # просто перегляд ціни
    order("молоко", "чай", buy=True)    # купівля
    order("молоко", "сіль", buy=True)   # один товар відсутній
    

if __name__ == '__main__':
    main()
            






