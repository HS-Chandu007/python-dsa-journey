
# PROBLEM: GRADE CALCULATOR

marks = float(input('Enter the Marks: '))


if marks >= 90:
    print('GRADE-A')
elif marks >= 80 and marks <= 89:
    print('GRADE-B')
elif marks >= 70 and marks <= 79:
    print('GRADE-C')
elif marks >= 60 and marks <= 69:
    print('GRADE-D')
elif marks < 0 and marks > 100:
    print('INVALID MARKS')
else:
    print('FAIL')