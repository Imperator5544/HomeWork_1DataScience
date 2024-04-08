import numpy as np

# Завдання 1: Створити масив розміром 3x3 зі значеннями від 0 до 8

arr1 = np.arange(9).reshape(3, 3)
print(arr1)

# Завдання2: Створитивекторрозміром10, заповненийнулями

arr2 = np.zeros(10)
print(arr2)

# Завдання 3: Створити вектор розміром 10, заповнений одиницями

arr3 = np.ones(10)
print(arr3)

# Завдання 4: Створити вектор розміром 10, заповнений значеннями 5
# Hints: np.full
arr4 = np.full(10, 5)
print(arr4)

# Завдання 5: Створити вектор з числами від 10 до 49

arr5 = np.arange(10,50)
print(arr5)

# Завдання 6: Реверсувати порядок елементів вектора з завдання 5
arr5 = np.arange(10, 50)
reversed_arr5 = np.flip(arr5)
print(reversed_arr5)

#Завдання 7: Створити 9x9 матрицю зі значеннями від 0 до 80
# Hints: np.arange
arr7 = sequence = np.arange(81)
matrix = sequence.reshape(9, 9)
print(matrix)

# Завдання 8: Знайти індекси ненульових елементів вектора [1,2,0,0,4,0]
# Hints: np.nonzero
arr8 = np.array([1, 2, 0, 0, 4, 0])
nonzero_indices = np.nonzero(arr8)
print(nonzero_indices)

#Завдання 9: Створити одиничну матрицю розміром 3x3
# Hints: np.eye
arr9 = np.eye(3)
print(arr9)

# Завдання 10: Створити випадковий вектор розміром 10 та відсортувати його
arr10 = np.random.rand(10)
arr10_sorted = np.sort(arr10)
print("Випадковий вектор:", arr10)
print("Відсортований вектор:", arr10_sorted)

# Завдання 11: Створити матрицю 5x5 з випадковими цілими числами в діапазоні від 0 до 10

arr11 = np.random.randint(0, 11, (5, 5))
print(arr11)

# Завдання 12: Обчислити суму всіх елементів матриці з завдання 11
arr12 = np.random.randint(0, 11, (5, 5))
arr11_sum = np.sum(arr12)
print(arr11_sum)

# Завдання 13: Знайти найменше значення в кожному рядку матриці з завдання 11

arr13 = np.random.randint(0, 11, (5, 5))
arr11_min_row = np.min(arr12, axis=1)
print(arr13)
print(arr11_min_row)

# Завдання 14: Обчислити середнє значення кожного стовпця матриці з завдання 11
arr14 = np.random.randint(0, 11, (5, 5))
arr11_mean_col = np.mean(arr14, axis=0)
print(arr11_mean_col)

# Завдання 15: Створити випадковий вектор розміром 15 та замінити максимальне значення на -1
# Hints: np.argmax
arr15 = np.random.rand(15)
max_index = np.argmax(arr15)
arr15[max_index] = -1
print(arr15)

# Завдання 16: Перетворити випадковий вектор розміром 10 в матрицю розміром 2x5
arr16 = np.random.rand(10)
matrix = arr16.reshape(2, 5)
print(arr16)
print(matrix)

# Завдання 17: Знайти середнє значення елементів матриці з завдання 16
arr16_mean = np.mean(matrix)
print(arr16_mean)