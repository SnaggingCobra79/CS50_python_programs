from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
font_list = figlet.getFonts()


if len(sys.argv) == 1:
    text = input("Input: ")
    f = random.choice(font_list)
    figlet.setFont(font=f)
    print(figlet.renderText(text))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
                i = sys.argv[2]
                if i in font_list:
                    text = input("Input: ")
                    figlet.setFont(font= i)
                    print(figlet.renderText(text))
                else:
                    sys.exit("Invalid Usage")
else:
       sys.exit("Invalid Usage")
