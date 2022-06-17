while True: 
  print("menu de inicio")
  print("escoja que quiere: ")
  print("reporte de fallas/pago/promociones")
  opcion=input()
 
  opcion1=("reporte de fallas")
  opcion2=("pago")
  opcion3=("promociones")

  if (opcion==opcion1):
    print("requiere fallas de red o television?: ")
    falla=input()
    if (falla=="a"):
      print("numero de reporte: 1234")
    else:
      print("numero de reporte: 9876")
    
  elif (opcion==opcion2):
    print("pago con tarjeta")
    print("inserte su numero de tarjeta: ")
    input()
    print("su pago ha sido completado 👍🏻")

  else: 
    print("las promociones del mes son: 2x1 en contrataciones, descuento en su pago si lo realiza con anticipacion")

    



