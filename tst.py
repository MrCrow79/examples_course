

class Car:

    base_class_name = [3,4]

    def __init__(self, brand: str, model: str, miles_limit: int = 0):
        self.__brand = brand
        self.__model = model
        self.__miles_limit = miles_limit
        self.__is_engine_started = False

    @property
    def miles_limit(self):
        return self.__miles_limit

    def start_engine(self):
        if not self.__is_engine_started:
            self.__is_engine_started = True
            return "Engine started."
        else:
            return "Engine is already running."

    def stop_engine(self):
        if self.__is_engine_started:
            self.__is_engine_started = False
            return "Engine stopped."
        else:
            return "Engine is already off."

    def drive(self, miles_to_drive: int):
        if self.__is_engine_started:
            if self.__miles_limit >= miles_to_drive:
                self.__miles_limit -= miles_to_drive
                return f"Driving {miles_to_drive} miles."
            else:
                return "The miles limit has been exceeded"
        else:
            return "Cannot drive. Engine is off."

    def present_your_self(self):
        print(f'Im {self.__brand}, {self.__model}')


class Audi(Car):

    brand = 'audi'

    def __init__(self, model, miles_limit):
        super().__init__(brand=__class__.brand, model=model, miles_limit=miles_limit)
        self.my_var = [1,2]


class Q8(Audi):

    def __init__(self):
        super().__init__(model='q8', miles_limit=500)
        self.my_var = [1,2]


my_base_car = Car('nissan', 'y61', 100)
my_car = Q8()
my_car1 = Q8()

# print(my_car.base_class_name)
# print(my_car1.base_class_name)
#
# my_car.__class__.base_class_name = 'New Car'
# print(my_car.__class__.base_class_name)
# print(my_car1.__class__.base_class_name)

# ____________________
print(id(my_car.base_class_name))
print(id(my_car1.base_class_name))
print(id(my_car.my_var))
print(id(my_car1.my_var))

# my_car.my_var = 'new_value'
#
# print(my_car.my_var)
# print(my_car1.my_var)