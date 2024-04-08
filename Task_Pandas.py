import pandas as pd

# Завдання 1: Створити серію зі списку чисел [10, 20, 30, 40, 50]
ser1 = pd.Series([10, 20, 30, 40, 50])
print(ser1)

# Завдання 2: Створити DataFrame зі списку списків [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(df2)

# Завдання 3: Задати індекси для серії з завдання 1 рядками "a", "b", "c", "d", "e"
# Hints: series.index
ser1 = pd.Series([10, 20, 30, 40, 50])
ser1.index = ["a", "b", "c", "d", "e"]
print(ser1)

# Завдання 4: Перейменувати стовпці DataFrame з завдання 2 на "A", "B", "C"
# Hints: df.columns
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df2.columns = ["A", "B", "C"]
print(df2)

# Завдання 5: Знайти максимальний елемент в серії з завдання 1
ser1 = pd.Series([10, 20, 30, 40, 50])
ser1_max = ser1.max()
print(ser1_max)

# Завдання 6: Знайти середнє значення для кожного стовпця DataFrame з завдання 2
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df2_mean = df2.mean()
print(df2_mean)


# Завдання 7: Знайти суму елементів в серії з завдання 1
ser1 = pd.Series([10, 20, 30, 40, 50])
ser1_sum = ser1.sum()
print(ser1_sum)

# Завдання 8: Вибрати всі рядки DataFrame з завдання 2, де значення стовпця "A" менше 5
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"])
df2_filtered = df2[df2["A"] < 5]
print(f"Значення стовпця менше п'яти", df2_filtered)

# Завдання 9: Додати новий стовпець "D" до DataFrame з завдання 2 зі значеннями [10, 20, 30]
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"])
df2["D"] = [10, 20, 30]
print(df2)

# Завдання 10: Видалити стовпець "B" з DataFrame з завдання 2
df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"])
df2 = df2.drop("B", axis=1)
print(df2)
