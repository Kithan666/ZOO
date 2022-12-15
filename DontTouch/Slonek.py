class Elephant:

    def __init__(self, name, age, foodPerDay):
        self.__name = name
        self.__age = age
        self.__foodPerDay = foodPerDay
        self.__isFeeded = False
        self.__foodEated = 0
        self.__species = "Elephant"
        self.__biome = "Desert"
        self.__areaPerIndividual = 500
        self.__foodTypes = ['trava', 'seno', 'frukti']
        self.__predator = False
        self.__sound = "Wooooo"

    @property
    def feeded(self):
        return self.__isFeeded

    def eat(self, foodType):
        if foodType not in self.__foodTypes:
            print(self.__name, 'said: Day drugoe, eto ne em')
            return

        if foodType in self.__foodTypes:
            if self.__foodEated >= self.__foodPerDay:
                print(self.__name, 'said: Ya yzhe naelsya')
                self.__isFeeded = True
                return
            else:
                print(self.__name, 'ate:', foodType)
                self.__foodEated += 1
                if self.__foodEated >= self.__foodPerDay:
                    print(self.__name,'said: Mne yzhe xvatit')
                    self.__isFeeded = True

    def doSound(self, number):
        for i in range(number):
            print(self.__name, "did:", self.__sound)

    def play(self):
        print(self.__name, "did: play")