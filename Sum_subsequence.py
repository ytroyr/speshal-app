start_t = int(input("Введите начальное число: "))
stop_t = int(input("Введите конечное число: "))
number_sum = 0
for number in range(start_t, stop_t + 1):
  number_sum += number
print("Сумма чисел от", start_t, "до", stop_t, "равна", number_sum)