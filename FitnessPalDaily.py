import myfitnesspal
import API_CONFIG
from datetime import date, timedelta, datetime
from collections import defaultdict


######
YESTERDAY = date.today() - timedelta(1)
YESTERDAY = YESTERDAY.strftime('%m%d%y')
######


class FitnessPalDaily:

    def __init__(self,):
        username = API_CONFIG.FITNESS_PAL_USERNAME
        password = API_CONFIG.FITNESS_PAL_PASSWORD
        self.client = myfitnesspal.Client(username, password)
        self.YESTERDAY = self.date_to_datetime()

    def date_to_datetime(self):
        return datetime.strptime(YESTERDAY, '%m%d%y')

    def get_yesterday_data(self):
        year, month, day = [self.YESTERDAY.year, self.YESTERDAY.month, self.YESTERDAY.day]
        return self.client.get_date(year, month, day)

    def get_nutrition(self, ):
        yesterday_nutrition = self.get_yesterday_data()
        daily_food_info = self.get_daily_nutrition_info(yesterday_nutrition)
        return daily_food_info

    def get_daily_nutrition_info(self, yesterday_nutrition):
        nutrition_dict = defaultdict(list)

        for counter, daily_meals in enumerate(yesterday_nutrition.meals):
            meal_name = self.get_meal_name(counter)

            statement_of_meal = self.format_meal_statement(meal_name, daily_meals.totals)
            nutrition_dict[meal_name].append(statement_of_meal)

            for meal in daily_meals:
                food_name = self.get_food_name(meal)
                statement_of_food = self.format_food_statement(food_name, meal)
                nutrition_dict[meal_name].append(statement_of_food)

        return nutrition_dict

    def format_food_statement(self, food_name, food_nutrition_info):
        macros = self.get_nutrition_info(food_nutrition_info)
        statement = (
            "    - Calories for {0} was {1} with a split in carbohydrates: {2}, fat: {3}, protein: {4},"
            "sodium: {5}, sugar: {6}.".format(food_name, macros[0], macros[1],
                                                macros[2], macros[3],
                                                macros[4], macros[5]))
        return statement

    def format_meal_statement(self, meal, meal_nutrition_info):
        macros = self.get_nutrition_info(meal_nutrition_info)
        statement = (
            "Daily Caloric intake for {0} was {1} with a split in carbohydrates: {2}, fat: {3}, protein: {4},"
            "sodium: {5}, sugar: {6}.".format(meal, macros[0], macros[1],
                                                macros[2], macros[3],
                                                macros[4], macros[5]))
        return statement

    def get_nutrition_info(self, nutrition):
        calories = self.get_calories(nutrition)
        carbs = self.get_carbohydrates(nutrition)
        fats = self.get_fat(nutrition)
        protein = self.get_protein(nutrition)
        sodium = self.get_sodium(nutrition)
        sugar = self.get_sugar(nutrition)
        return [calories, carbs, fats, protein, sodium, sugar]

    def get_calories(self, food):
        try:
            calories = food['calories']
        except KeyError:
            calories = 0
        return calories

    def get_carbohydrates(self, food):
        try:
            calories = food['carbohydrates']
        except KeyError:
            calories = 0
        return calories

    def get_fat(self, food):
        try:
            calories = food['fat']
        except KeyError:
            calories = 0
        return calories

    def get_protein(self, food):
        try:
            calories = food['protein']
        except KeyError:
            calories = 0
        return calories

    def get_sodium(self, food):
        try:
            calories = food['sodium']
        except KeyError:
            calories = 0
        return calories

    def get_sugar(self, food):
        try:
            calories = food['sugar']
        except KeyError:
            calories = 0
        return calories

    def get_meal_name(self, meal_num):
        return "Meal {0}".format(meal_num+1)

    def get_food_name(self, meal):
        return meal.name

    @staticmethod
    def upload_yesterday():
        f = FitnessPalDaily()
        return f.get_nutrition()
