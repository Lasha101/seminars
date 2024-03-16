# class Calculator:
#     class PercentCalc:
#         @staticmethod
#         def init_amount(num, prc):
#             result = num / (1 - prc / 100)
#             return f"init_amount: {round(result, 1)}"
        
#         @staticmethod
#         def num_to_percent(num, prc):
#             result = (prc / num) * 100
#             return f"num_to_percent: {round(result, 2)}"
        
#         @staticmethod
#         def percent_to_num(num, prc):
#             result = (num * prc) / 100
#             return f"percent_to_num: {round(result, 1)}"
#     class CompareCalc:
#         @staticmethod
#         def diff_calc(num1, num2):
#             diff = num1 - num2
#             return f"diff_calc: {diff}"
        
#         @staticmethod
#         def times_calc(num1, num2):
#             times = num1 / num2
#             return f"times_calc: {round(times, 2)}"
        
#         @staticmethod
#         def part_of_num(num1, num2):
#             part = num2 / num1
#             return f"part_of_num: {round(part, 1)}"
        
#     @classmethod
#     def calculate(cls, num_dict):
#         results = []

#         for key, value in num_dict.items():
#             if "%" in str(key):
#                 prc = float(key.strip("%"))
#                 num = float(value)
#                 if 0 <= prc <= 100:
#                     result = cls.PercentCalc.init_amount(num, prc), \
#                              cls.PercentCalc.num_to_percent(num, prc), \
#                              cls.PercentCalc.percent_to_num(num, prc)
#                 else:
#                     continue
#             else:
#                 num1 = float(key)
#                 num2 = float(value)
#                 result = cls.CompareCalc.diff_calc(num1, num2), \
#                          cls.CompareCalc.times_calc(num1, num2), \
#                          cls.CompareCalc.part_of_num(num1, num2)
                
#             results.append((key, value, result))
#         return results


# num_dict = {"10":"15", "50":"124", "20%":"77", "17":"80"}

# results = Calculator.calculate(num_dict)

# for i in results:
#     print(i)
                









# class PercentCalc:
#     def __init__(self, num, prc):
#         self.num = num
#         self.prc = prc
        
#     @classmethod
#     def init_amount(cls, num, prc):
#         result = num / (1 - prc / 100)
#         return f"init_amount: {round(result, 1)}"

#     @staticmethod
#     def part_of_num(num1, num2):
#         part = num2 / num1
#         return f"part_of_num: {round(part, 1)}"
    
#     def __str__(self):
#         return self.init_amount(self.num, self.prc)
    

# init = PercentCalc(100, 15)

# print(init)
    
# print(PercentCalc.part_of_num(100, 20))

        
    


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._area = width * height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
        self._area = self._width * self._height 

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
        self._area = self._width * self._height 

    @property
    def area(self):
        return self._area
    
rect = Rectangle(3, 4)
print(rect.area)

# rect.width = 5
# print(rect.area)


    



















