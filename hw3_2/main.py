# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
 

def max_collected_berries(berries):
    n = len(berries)
    max_collected = 0

    for i in range(n):
        collected = berries[i] + berries[(i + 1) % n] + berries[(i + 2) % n]
        max_collected = max(max_collected, collected)

    return max_collected

# Считывание данных
n = int(input("Введите количество кустов: "))
berries = []

print("Введите количество ягод на каждом кусте:")
for _ in range(n):
    berries.append(int(input()))

result = max_collected_berries(berries)
print("Максимальное количество ягод, которое может собрать собирающий модуль:", result)
