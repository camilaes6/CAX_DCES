import datetime

dia=datetime.date.today()

w=dia.weekday()+1

if(w==0):
  print("feliz domingo")

elif (w==1):
  print("es lunes yupiii")

elif (w==2):
  print("es martes wuujuuu")

elif (w==3):
  print("animo es miercoles")

elif (w==4):
  print("es jueves, casi viernes yay")

elif (w==5):
  print("venga es viernes!")

else:
  print("yuju es sabado")
