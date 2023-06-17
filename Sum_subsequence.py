while True:
  start_n = int(input("Введите начальное число: "))
  stop_n = int(input("Введите конечное число: "))
  number_sum = 0
  for number in range(start_n, stop_n + 1):
    number_sum += number
  print("Сумма чисел от", start_n, "до", stop_n
        , "равна", number_sum)