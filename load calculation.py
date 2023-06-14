while True:
  update = float(input("Введите размер загрузки (в МБ): "))
  internet = float(input("Введите скорость интернет подключения (в МБ/с): "))
  download = 0
  prosent = update * 0.01
  sec = 0

  while download < update:
    while True:
      sec += 1
      download += internet
      if download == update:
        download = update
      elif download > update:
        download = update
      now_prosent = round(download / prosent)
      print("Прошло", sec, "секунд")
      print("Загружено", int(download), "из", int(update), "(",now_prosent,"%)")
      if download == update:
        break