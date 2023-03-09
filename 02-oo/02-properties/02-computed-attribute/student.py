class BMICalculator:

    def __init__(self,weight_in_kg,height_in_m):
        self.weight = weight_in_kg
        self.height = height_in_m

    def bmi(self):
        bmi = self.weight / self.height**2
        return float(f'{bmi:.2f}')
    
    def category(self):
        if self.bmi() < 18.5:
            return "underweight"
        elif self.bmi() >= 18.5 and self.bmi()<= 25:
            return "normal"
        elif self.bmi() > 25:
            return "overweight"
        

calc = BMICalculator(weight_in_kg=80, height_in_m=1.80)
print(calc.bmi())
print(calc.category())