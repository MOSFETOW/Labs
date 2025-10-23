

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
    {"хліб": True, "ціна": 13},
    {"молоко": True, "ціна": 123},
    {"яйця": True, "ціна": 17},
    {"цукор": True, "ціна": 56},
    {"сіль": False, "ціна": 97},
    {"масло": False, "ціна": 12.50},
    {"сир": True, "ціна": 89},
    {"ковбаса": True, "ціна": 54},
    {"борошно": True, "ціна": 76.09},
    {"чай": True, "ціна": 123}]


#Перевіряє наявність  товарів у магазині
def check_availability(*products):
    result = {}
    for product in products:
        result.update({product:False})
        for select_item in store_items:           
            if select_item.get(product):
                result[product]=True
                continue   
    return result









def order(*args, option=False):
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
    if not option:
        print(f"Загальна вартість вибраних товарів: {total} грн.")
        return

    # Якщо користувач хоче купити
    if option and available:
        print(f"Замовлення прийнято! {total} грн.")
    else:
        print("Замовлення неможливе, бо товари відсутні.")

def main():



    # Приклад використання
    print(format_price(123.4))
    print(format_price(1.47467))
    print(format_price(353))  
    
    
    print(check_availability("сир","хліб", "яблука", "чай"))




    
    # приклади використання:
    order("молоко", "чай", option=False)   # просто перегляд ціни
    order("молоко", "чай", option=True)    # купівля
    order("молоко", "сіль", option=True)   # один товар відсутній
    

if __name__ == '__main__':
    main()
