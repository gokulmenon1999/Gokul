import random

class AutonomousVehicle:
    def _init_(self):
        self.speed = 0
        self.obstacle_detected = False
    
    def accelerate(self):
        self.speed += 1
    
    def brake(self):
        self.speed -= 1 if self.speed > 0 else 0
    
    def detect_obstacle(self):
        
        self.obstacle_detected = random.choice([True, False])
    
    def navigate(self):
        if self.obstacle_detected:
            print("Obstacle detected! Navigating around...")
            
            self.brake()
        else:
            print("No obstacles detected. Continuing on route...")
            self.accelerate()


car = AutonomousVehicle()


for _ in range(10):
    car.detect_obstacle()
    car.navigate()
    print("Current speed:", car.speed)
    print("------------------------")
