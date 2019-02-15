from time import sleep
from random import randint
from threading import Thread
from colorama import init, Fore, Style
from rprint import print

#40Hz - 1kHz
class Arm(Thread):
    id = 0
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE,
              Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]
    stepmotor_coeff = 100
    distances = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1,
                 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1}
    def __init__(self):
        self.id = Arm.getId()
        super().__init__(name = self.id)
        self.color = Arm.colors[self.id - 1] 
        self.pos = 0
        self.ready = False
        self.tic = 0
        self.IMPULSES_PER_DISTANCE = 1
        self.pprint('Initialized arm {}')

    #Utility, for testing use!------------------------------#
    def getId():
        Arm.id+=1
        return Arm.id

    def pprint(self, string):
        print(self.color + string.format(self.id) + '\r',
              flush=True)
        #print(string.format(self.id))
    #-------------------------------------------------------#

    #Timing based functions---------------------------------#
    def nextTic(self):
        self.strum()
        self.increaseTic()

    def strum(self):
        self.pprint("strum string {}")

    def increaseTic(self):
        self.tic += 1
    #-------------------------------------------------------#

    #Run sequence, in order of execution--------------------#
    def setNotes(self, notes):
        self.notes = notes
        self.ready = True

    def run(self):
        self.pprint('Running arm {}')
        self.initMovement()
    
    def initMovement(self):
        if self.ready:
            self.pprint(str(self.notes))
            for note in self.notes:
                self.pprint("from " + str(self.pos) + " to " + str(note[0]) + " until " + str(note[1]))
                self.moveTo(note[0])
                while note[1] >= self.tic:
                    sleep(0.1)
        else:
            self.pprint("No notes available to play!")

    def moveTo(self, destination):
        delta = abs(self.pos - destination)
        impulses = delta * self.IMPULSES_PER_DISTANCE
        self.pprint('Arm {}: '+'{} impulses'.format(impulses))
        self.pos = destination
    #-------------------------------------------------------#

class Supervisor:
    def __init__(self):
        self.arms = []
        self.tic_time = 1

    def addArms(self, arms):
        self.arms += arms

    def runArms(self):
        for arm in self.arms:
            arm.start()
        self.tic()

    def tic(self):
        tic = 0
        print("tic " + str(tic))
        sleep(1)
        while tic < 13:
            for arm in self.arms:
                arm.nextTic()
            print("tic " + str(tic))
            tic += 1
            sleep(self.tic_time)

    def genRan(self):
        tuples = []
        for tupl in range(12):
            tuples += [(randint(-1, 3), tupl)]

        better_tuple = []
        sorting = True
        while sorting:
            if len(tuples) == 1:
                t1, t2 = tuples[0], ['X']
            else:
                t1, t2 = tuples[0], tuples[1]
                
            if t1[0] == t2[0]:
                tuples = tuples[1:]
            else:
                better_tuple += [tuples[0]]
                tuples = tuples[1:]

            if len(tuples) == 0:
                sorting = False

        return better_tuple

if __name__ == "__main__":
    init()
    supervisor = Supervisor()

    arms = []
    for num in range(2):
        current_arm = Arm()
        current_arm.setNotes(supervisor.genRan())
        arms += [current_arm]

    supervisor.addArms(arms)
    supervisor.runArms()
