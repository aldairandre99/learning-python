
def calculete_area(w,h):
  area = w * h
  print(f"\nThe total Sqft is: {area}\n")

print("\nPlease enter the dimension of the room in sqft")

width = int(input("\nPlease enter the width of the room: "))
height = int(input("\nPlease enter the height of the room: "))

calculete_area(width,height)