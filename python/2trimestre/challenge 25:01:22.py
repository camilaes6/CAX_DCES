grade1=int(input("insert your first grade:  "))
grade2=int(input("insert your second grade: "))
grade3=int(input("insert your third grade: "))
finalgrade=(grade1+grade2+grade3)/3
print("your average is:", finalgrade)
if (finalgrade>6):
 print("congrats you passed the year")

while True:

 if (finalgrade<6):
  print("oh im sorry you failed")

 if (finalgrade==9):
  print("congratulations you won a medal and diploma for excellence")