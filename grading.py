your_grade = input('What percentage grade did you get? ')
your_grade = int(your_grade)
plus_minus = your_grade % 10
if your_grade >= 90:
    if plus_minus < 5:
        print("You got an 'A-'!")
    elif plus_minus >= 5:
        print("You got an 'A+'!")
elif your_grade >= 80:
    if plus_minus < 5:
        print("You got a 'B-'!")
    elif plus_minus >= 5:
        print("You got a 'B+'!")
elif your_grade >= 70:
    if plus_minus < 5:
        print("You got a 'C-'!")
    elif plus_minus >= 5:
        print("You got a 'C+'!")
elif your_grade >= 60:
    if plus_minus < 5:
        print("You got a 'D-'!")
    elif plus_minus >= 5:
        print("You got a 'D+'!")
elif your_grade < 60:
    print("You got an 'F'!")
