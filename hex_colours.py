def main():
    color_to_hex = {'AliceBlue' : '#f0f8ff','AntiqueWhite': '#faebd7', 'AntiqueWhite1':'#ffefdb',
                    'AntiqueWhite2':'#eedfcc','AntiqueWhite3':'#cdc0b0','AntiqueWhite4':'#8b8378',
                    'aquamarine1':'#7fffd4','aquamarine2':'#76eec6','azure1':'#f0ffff','aquamarine4':'#458b74'}
    while True:
        color = str(input("Color name:"))
        for key,value in color_to_hex.items():
            if color.lower() == key.lower():
                print(color_to_hex[key])
                quit()
        if key not in color_to_hex:
            print("No matching data found. Please try again.")
main()