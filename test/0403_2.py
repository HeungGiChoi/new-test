# 건강상태 실습 3.
## protect, getter, setter 사용해보기

class Health:
    def __init__(self, name, hp, exercise, alchole):
        self.__exercise = exercise
        self.__alchole = alchole
        self.hp = hp
        self.name = name

    #getter_exercise
    @property
    def exercise(self):
        return self.__exercise
    
    #setter_exercise
    @exercise.setter
    def exercise(self, exercise):
        self.__exercise = exercise

    #getter_alchole
    @property
    def alchole(self):
        return self.__alchole
    
    #setter_alchole
    @alchole.setter
    def alchol(self, alchole):
        self.__alchole = alchole
    
    def exer_alc(self):
        for i in range(self.__exercise):
            self.hp += 1
        for i in range(self.__alchole):
            self.hp -= 1

health1 = Health("나몸짱", 95, 5, 2)
health2 = Health("나약해", 11, 1, 12)

health1.exer_alc()
health2.exer_alc()

print(health1.exercise, "시간 운동하다")
print("술을", health1.alchole, "잔 마시다.")
print(health1.name, "- hp : ", health1.hp)