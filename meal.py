
class Meal:

    def __init__(self,name,carbs,proteins,fats):
        self.name=name
        self.carbs=carbs
        self.proteins=proteins
        self.fats=fats

    def __str__(self):
        result = "{}, carbs {}g, proteins {}g, fats {}g".format(self.name, self.carbs, self.proteins, self.fats)
        return result
    
    def calculate_meal_kcal(self):
        return (self.carbs *4 ) +(self.proteins * 4) + (self.fats * 9)
    