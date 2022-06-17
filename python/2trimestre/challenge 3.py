while True:
  speed=int(input("insert your speed: "))

  if (speed>25):
   print("alerta critica")

  elif (speed>10):
   print("estrella fugaz")

  elif (speed==20):
   print("rayo en el cielo")

  else:
   print("nada que ver")