"""
6)Furniture:

Household type, total area and furniture name listThe new house has no furniture at all.
Furniture has a name and area, of whichBed: 4 square metersWardrobe: 2 square metersTable:
1.5 square meters
Add the above three pieces of furniture to the house
When printing a house, output is required: household type, total area, remaining area,
furniture name list.
"""
class Home:
    
    def __init__(self, all_furniture, area = 80):
        self.all_furniture = all_furniture
        self.bed = all_furniture[0]
        self.sofa = all_furniture[1]
        self.wardrope = all_furniture[2]
        self.table = all_furniture[3]
        self.chairs = all_furniture[4]
        self.area = area
    
    def __str__(self):
        return f"в доме площадью {self.area}m*2, установлена мебель: {', '.join(self.all_furniture)}"
       
    
    def furniture_area(self,bed,sofa,wardrope,table,chair):
        self.furniture_area = bed + sofa + wardrope + table + chair
        print(f"площадь занимаемая мебелью {self.furniture_area :.1f} м2")
    
    def free_area(self):
        self.free_area = self.area - self.furniture_area
        print(f"Общая площадь дома {self.area}, площадь занимаемая мебелью {self.furniture_area :.1f}, свободной площади осталось {self.free_area}")

all_furniture = ["Кровать", "диван", "гардероб", "Стол","стул"]
house = Home(all_furniture, 155)
print(house)
house.furniture_area(4, 3.5, 2, 1.4, 0.3)
house.free_area()
