def main():
    COLOR_TO_HEX= {'AliceBlue' : '#f0f8ff','AntiqueWhite': '#faebd7', 'AntiqueWhite1':'#ffefdb',
                    'AntiqueWhite2':'#eedfcc','AntiqueWhite3':'#cdc0b0','AntiqueWhite4':'#8b8378',
                    'aquamarine1':'#7fffd4','aquamarine2':'#76eec6','azure1':'#f0ffff','aquamarine4':'#458b74'}
    while True:
        color = str(input("Color name:"))
        for key,value in COLOR_TO_HEX.items():
            if color.lower() == key.lower():
                print(COLOR_TO_HEX[key])
                quit()
            elif key not in COLOR_TO_HEX:
                print("No matching data found. Please try again.")
main()