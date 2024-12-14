class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name  # 修正屬性名稱
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print('Restaurant is open')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)  # 修正 super 的用法
        self.flavors = ['berry', 'wine', 'cake']


# 創建 Restaurant 實例
restaurant_information = Restaurant('Ben', 'Steak')
restaurant_information2 = Restaurant('LEP0', 'DDD')

print('The restaurant name is ' + restaurant_information.restaurant_name +
      " and it serves " + restaurant_information.cuisine_type)
print('The restaurant name is ' + restaurant_information2.restaurant_name +
      " and it serves " + restaurant_information2.cuisine_type)

# 創建 IceCreamStand 實例
ice_cream_stand = IceCreamStand('Icey Delight', 'Dessert')
print(ice_cream_stand.flavors)  # 從 IceCreamStand 實例訪問 flavors
