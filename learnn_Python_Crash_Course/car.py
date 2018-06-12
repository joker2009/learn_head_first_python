__author__ = 'joker_jiang'


class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的小心"""
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        """将里程表的读书设置为指定的值,禁止回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odomenter!")
        # self.odometer_reading = mileage
    def increment_odometer(self, miles):
        """将里程表读数增加 """
        self.odometer_reading += miles


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电池属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一天描述电池容量的消息"""
        print("This car has a " + str(self.battery_size) + " kWh battery")

    def get_range(self):
        """打印一条消息，支出电瓶的续航力场"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."
        print(message)


class ElectricCar(Car):
    """电动车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动车特有的属性"""
        super().__init__(make, model, year)

        # self.battery_size = 70
        self.battery = Battery()

    # def describe_battery(self):
    #     """打印一天描述电瓶容量的信息"""
    #     print("This car has a " + str(self.battery_size) + " kWh battery")


if __name__ == "__main__":

    my_tesla = ElectricCar('tesla', 'model s', 2017)
    print(my_tesla.get_descriptive_name())
    # my_tesla.describe_battery()
    my_battery = Battery(85)
    my_battery.describe_battery()
    # my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.read_odometer()
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_new_car.update_odometer(25)
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(24)
# my_new_car.read_odometer()