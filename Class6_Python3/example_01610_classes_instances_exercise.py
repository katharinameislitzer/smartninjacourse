class Robot:
    def __init__(self, model, mission, color="Blue"):
        self.model = model
        self.mission = mission
        self.color = color


    def __str__(self):
        return f"Robot(model={self.model}, mission{self.mission}, color={self.color})"

# create 1 instance of Robot
# give it a the model "HAL9000"
# give it the mission "protect humans"
# print its model
# print its mission

x = Robot("model: HAL9000", "mission: protect humans")
print(x.model)
print(x.mission)

robot_1 = Robot("model: HAL9000", "mission: protect humans")
robot_2 = Robot("model: HAL9000", "mission: protect humans", "Red")
robot_3 = Robot("model: HAL9000", "mission: protect humans", color="Green")
print(robot_1.color)
print(robot_2.color)
print(robot_3.color)
