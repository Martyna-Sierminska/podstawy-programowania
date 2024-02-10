class KcalCalculator:
# PPM mężczyzny = 66,47 + (13,7 x masa ciała w kg) + (5 x wzrost w cm] – [6,76 x wiek w latach]
#  PPM dla kobiety = 655,1 + (9,567 x masa ciała w kg) + (1,85 x wzrost w cm) – (4,68 x wiek w latach)


    def calculate_kcal(dictionary_person):
        if dictionary_person["gender"] == "M":
            result = 66.47 + (13.7 * dictionary_person["weight"]) + (5 * dictionary_person["height"]) - (6.76 * dictionary_person["age"])
        else :
            result = 655.1 + (9.567 * dictionary_person["weight"]) + (1.85 * dictionary_person["height"]) - (4.68 * dictionary_person["age"])
        
        return int(result)
