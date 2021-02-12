VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    
    """In the while loop ask lowerthe user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        get_color = input("Please enter a color: ")

        lower_color = get_color.lower()
      
        if lower_color == "quit":
            print("bye")
            break

        for color in VALID_COLORS:
            if lower_color in VALID_COLORS:
                print(lower_color)
                break
            else: print("Not a valid color")

print_colors()           