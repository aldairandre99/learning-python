# Converting data
import time

year = time.localtime().tm_year
name = "Aldair"
birthdate = "1999"

print(f"\n\nHello\n\n{name}, you are now {year - int(birthdate)} years old\n\n")
