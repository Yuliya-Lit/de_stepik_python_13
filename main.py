import ast

try:
    # Пытаемся открыть и прочитать файл
    with open("data.txt", "r", encoding='utf-8') as file:
        content = file.read()

    file_purchases = []
    for item in content.split(",\n"):
        item = item.strip()
        if item:
            try:
                parsed_item = ast.literal_eval(item)
                file_purchases.append(parsed_item)
            except (SyntaxError, ValueError) as e:
                print(f"Ошибка при обработке элемента '{item}': {e}")


    def total_revenue(purchases):
        sum = 0
        for i in purchases:
            sum += i.get("price") * i.get("quantity")
        return sum


    def items_by_category(purchases):
        my_dict = dict()
        for i in purchases:
            if i.get("category") in my_dict:
                my_dict[i.get("category")].append(i.get("item"))
            else:
                my_dict[i.get("category")] = [i.get("item")]
        return my_dict


    def expensive_purchases(purchases, min_price):
        alist = []
        for i in purchases:
            if i.get("price") > min_price:
                alist.append(i)
        return f"Покупки дороже {min_price}: {alist}"


    def average_price_by_category(purchases):
        my_dict = dict()
        res = dict()

        for i in purchases:
            if i.get("category") in my_dict:
                my_dict[i.get("category")].append(i.get("price"))
            else:
                my_dict[i.get("category")] = [i.get("price")]

        for key, value in my_dict.items():
            res[key] = sum(value) / len(value)
        return res


    def most_frequent_category(purchases):
        my_dict = dict()

        for i in purchases:
            if i.get("category") in my_dict:
                my_dict[i.get("category")] += i.get("quantity")
            else:
                my_dict[i.get("category")] = i.get("quantity")
        return max(my_dict, key=my_dict.get)


    # Открываем файл для записи
    file = open("res.txt", "w", encoding='utf-8')

    # Записываем строку
    file.write(f"Общая выручка: {total_revenue(file_purchases)}\n")
    file.write(f"Товары по категориям: {items_by_category(file_purchases)}\n")
    file.write(f"{expensive_purchases(file_purchases, 1.0)}\n")
    file.write(f"Средняя цена по категориям: {average_price_by_category(file_purchases)}\n")
    file.write(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(file_purchases)}\n")

    # Закрываем файл
    file.close()

except FileNotFoundError:
    # Обработка, если файла нет
    print("Файл не найден.")
except Exception as e:
    # Обработка всех других возможных ошибок
    print("Произошла ошибка:", e)
