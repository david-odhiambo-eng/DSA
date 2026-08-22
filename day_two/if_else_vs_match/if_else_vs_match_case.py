#calculating students grades(match-case statememnts)
def calculate_grade(marks: int):
    
    try:
        int_marks = int(marks)
            
        is_E = int_marks <= 39
        is_D = int_marks >= 40 and int_marks <= 49
        is_C = int_marks >= 50 and int_marks <= 59
        is_B = int_marks >= 60 and int_marks <= 69
        is_A = int_marks >= 70 and int_marks <= 100
        
        match marks:
            case _ if is_E:
                print('You scored E')
            case _ if is_D:
                print('Your grade is D')
            case _ if is_C:
                print('Your grade is C')
            case _ if is_B:
                print('Your grade is B')
            case _ if is_A:
                print('Your grade is A')
            case _:
                print('Invalid input')
    except:
        print('An error has occurres')        

marks = input('Enter marks: ')
calculate_grade(marks=marks)