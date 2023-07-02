class Room:
    length = 0.0
    breadth = 0.0

    #method to calculate  area
    def calculate_area(self):
        print('Area of Room =',self.length * self.breadth)

#create object of Room class
study_room =  Room()

# assign values to all the attributes
study_room.length = 22.3
study_room.breadth = 12.0

# access method inside class
study_room.calculate_area()