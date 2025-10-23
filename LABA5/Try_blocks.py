import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
    
def main():
    # 1. requests — простий HTTP-запит
    try:
        
        response = requests.get("https://api.github.com")
        print("requests: Статус-код =", response.status_code)
    except Exception as e:
        print("Помилка в requests:", e)
    
    
    # 2. numpy — створення масиву і базові операції
    try:
        
        arr = np.array([1, 2, 3, 4, 5])
        print("numpy: Сума елементів =", np.sum(arr))
    except Exception as e:
        print("Помилка в numpy:", e)
    
    
    # 3. pandas — створення простого DataFrame
    try:
        
        data = {"Ім'я": ["Анна", "Іван"], "Вік": [23, 30]}
        df = pd.DataFrame(data)
        print("pandas:\n", df)
    except Exception as e:
        print("Помилка в pandas:", e)
    
    
    # 4. matplotlib — побудова простої діаграми
    try:
       
        plt.plot([1, 2, 3], [2, 4, 6])
        plt.title("Простий графік")
        plt.show()
        print("matplotlib: графік відображено")
    except Exception as e:
        print("Помилка в matplotlib:", e)
    
    
    # 5. Pillow — створення простого зображення
    try:
        
        img = Image.new("RGB", (100, 100), color="lightblue")
        draw = ImageDraw.Draw(img)
        draw.text((10, 40), "Hi!", fill="black")
        img.show()
        print("Pillow: зображення створено")
    except Exception as e:
        print("Помилка в Pillow:", e)


if __name__ == '__main__':
    main()


