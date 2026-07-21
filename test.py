def calculate_area(l: int, w: int):
    area = l * w
    print(f'Area is {area}cm^2 ')
    return area

while True:
    l = input('Enter length: ')
    w = input('Enter width: ')  

    try:
        length = int(l)
        width = int(w)
        calculate_area(length, width)
        break
    except ValueError:
        print('Try again, integers only')


    


    


