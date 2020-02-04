class Vehicle():

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
        self.isOn = False
        self.isMovement = False

    def __str__(self):
        data = '\n Brand: ' + self.brand + '\nModel: ' \
        + self.model + '\n'   
        return data


class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.type = type
        self.acelerate_car = acelerate

    def turn_on(self):
        self.isOn = True
        print ('Now the car is turned on')

    def movement(self):
        if self.isOn = True:
            self.isMovement = True
            self.acelerate()
        else:
            print('The car is must in movement')

    def acelerate_car(self):
        if self.isOn and self.isMovement:
            self.speed += self.acelerate
            print('Now the car is in movement, its speed is: ', self.speed)
        elif self.isOn:
            print('The car must be in movement')
        else:
            print('You must turn on the car and acelerate it') 

    def __str__(self):
        data = super().__str_()
        if self.isOn:
            data += 'The car is turned on\n'
            if.self.Movement:
                data += 'Its speed is ' + str(self.speed) + 'm/s.\n'
        return data








        #import random                                                






































