def main():
    color = str(input("Color name:"))
    COLOR_TO_HEX= {'aliceblue' : '#f0f8ff','antiquewhite': '#faebd7', 'antiqueWhite1':'#ffefdb',
                    'antiquewhite2':'#eedfcc','antiquewhite3':'#cdc0b0','antiqueWhite4':'#8b8378',
                    'aquamarine1':'#7fffd4','aquamarine2':'#76eec6','azure1':'#f0ffff','aquamarine4':'#458b74'}
    status = False
    while not status:
        if color.lower() in COLOR_TO_HEX:
            print(COLOR_TO_HEX[color])
            color = str(input("Color name:"))
        elif color == "":
            print("Thanks, bye")
            status = True
        else:
            print("That is not in our database, please try another")
            color = str(input("Color name:"))
main()