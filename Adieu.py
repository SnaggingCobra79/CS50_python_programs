import inflect
import sys
p = inflect.engine()

names = []
try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    print()
    pass
if not names:
    sys.exit("NO names")

formatted = p.join(names)
print(f"Adieu, adieu, to {formatted}")
