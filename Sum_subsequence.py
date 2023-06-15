While True:
  start = int(input("Введите начальное число: "))
  stop = int(input("Введите конечное число: "))
  number_sum = 0
  for number in range(start, stop + 1):
    number_sum += number
  print("Сумма чисел от", start, "до", stop, "равна", number_sum)
