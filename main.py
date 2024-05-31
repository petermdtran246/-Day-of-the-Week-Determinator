def DayName(day):
    match day:
        case 1:
            print('sun')
        case 2:
            print('mon')
        case 3:
            print('tue')
        case 4:
            print('wed')
        case 5:
            print('thu')
        case 6:
            print('fri')
        case 7:
            print('sat')
        case _:
            print('Invalid day')

day = int(input('Enter the day number: '))
DayName(day)