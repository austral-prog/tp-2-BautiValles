def earth():
    x = "Bangladesh"
    y = "Barbados"
    ToF1 = bool()
    ToF2 = bool()
    if len(x)<len(y):
        longitud = len(x)
    else:
        longitud = len(y)

    for i in range(longitud):
        if x[i] < y[i]:
            ToF1 = True
            ToF2 = False
            print(f"The result of {x} comes first in the dictionary than {y} is {ToF1}.")
            print(f"The result of {y} comes first in the dictionary than {x} is {ToF2}.")
            break
        elif y[i] < x[i]:
            ToF1 = True
            ToF2 = False
            print(f"The result of {x} comes first in the dictionary than {y} is {ToF1}.")
            print(f"The result of {y} comes first in the dictionary than {x} is {ToF2}.")
            break
