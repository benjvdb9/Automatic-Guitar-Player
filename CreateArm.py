from AGP import Supervisor, Arm

sup = Supervisor()
Arm1 = Arm()

notelists = sup.genRan()
print(notelists)

Arm1.setNotes(notelists)

sup.addArms([Arm1])
sup.runArms()