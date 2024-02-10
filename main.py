
from calculator_kcal import *
from meal import *
from recepies import *
import random



def check_if_number(number):          #To Jest Funkcja sparwwdza czy to podał jest liczbą ale zostawia stringa ( bo inputy zawsze stringi) w liczbę większą od 0
    res = False

    try:
        number = int(number)
        if number > 0:
            res = True
    except Exception:
        pass
        
    return res


if __name__=="__main__":               #To jest pocztek programu zawsze tak wygląda

    print("Hi")
    print( "Please enter your name")
    firstname =input ()
    print("Hello " + firstname)
    #Z tego wyszłam :
    # print("What is your weight in full kg ?")
    # weight=input()

    # if check_if_number(weight) is False:
    #     print("Invalid weight")
        
    check = False #zmienna pomocnica To jest po to żeby wykonywał pętlę do skutku 
                   #aż input nie bedą prawidłowe(liczba) zawiera tą funkcję z góry
    while check is False:
        print("What is your weight in full kg ?")
        weight=input()
        check = check_if_number(weight)

        if check is False:
            print("Invalid weight")

    check=False
    while check is False:
        print("What is your height in cm ?")
        height = input()
        check = check_if_number(height)

        if check is False:
            print("Invalid numer")
   

    check=False
    while check is False:
        print( "How old are you?")
        age=input()
        check=check_if_number(age)
        if check is False:
            print("Invalid number")


    check= False
    while check is False:
        print("What is your gender? [M - male] [F - female]")
        gender=input()
        gender=gender.upper()
        if gender != "M" and gender != "F":
            print("Invalid Gender")
        else:
            check = True

        
    dictionary_person={
        "name": firstname,
        "weight" : int(weight),
        "height" : int(height),
        "age": int(age),
        "gender": gender,
    }

    meal_list = []    # tworze liste pustą
    for meal_name in RECEPIES_NAMES: # meal_name to alias i sukam w liscie stringów w RECEPIES NAME
        carbs = random.randint(10, 100)
        proteins = random.randint(10, 100)
        fats = random.randint(10, 100)
        meal_list.append(Meal(meal_name, carbs, proteins, fats)) # do pustej listy meal list dodaje obiekty z klasy Meal 
                                                # Jak ta pentla pierwsza for prejdzie cała to meal list jest pełna obiektów

    print("Your kcal limit is: ", KcalCalculator.calculate_kcal(dictionary_person))

    kcal_limit = KcalCalculator.calculate_kcal(dictionary_person)

    sum_of_kcal = 0
    proposed_meals = []
    cnt = 0
    found = False
    lower_bound = int(kcal_limit * 0.9)
    upper_bound = int(kcal_limit * 1.1)

    print("Searching meals set in range from {} to {}...".format(lower_bound, upper_bound))
    while found is False:
        if cnt == 1000:
            break

        for x in range(3):
            i = random.randint(0, len(meal_list) - 1)
            while meal_list[i] in proposed_meals:
                i = random.randint(0, len(meal_list) - 1)
            sum_of_kcal += meal_list[i].calculate_meal_kcal()
            proposed_meals.append(meal_list[i])

        if sum_of_kcal <= upper_bound and sum_of_kcal >= lower_bound:
            found = True
            break
        else:
            sum_of_kcal = 0
            proposed_meals.clear()
            cnt += 1

    if found is False:
        print("Sorry, I couldn't find a meal set to fit your needs :(, I don't have enough recipes...Try again, maybe I'll generate better random recepies ;)")
        exit(1)
    
    print("Here is your list of recepies for the day, total kcal {}:".format(sum_of_kcal))
    for meal in proposed_meals:
        print(meal)

    exit(1)

       

