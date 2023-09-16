from gasfun import *
import numpy as np
from datetime import datetime


win = GraphWin("Perfect gas simulation",380,380)
win.master.geometry('%dx%d+%d+%d' % (380, 380, 1000,200))

r = 2
vel = 25

circ1 = Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ1.filll("black")
circ1.Drw(win)

circ2 = Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ2.filll("black")
circ2.Drw(win)

circ3= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ3.filll("black")
circ3.Drw(win)

circ4= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ4.filll("black")
circ4.Drw(win)

circ5= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ5.filll("black")
circ5.Drw(win)

circ6= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ6.filll("black")
circ6.Drw(win)

circ7= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ7.filll("black")
circ7.Drw(win)

circ8= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ8.filll("black")
circ8.Drw(win)

circ9= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ9.filll("black")
circ9.Drw(win)

circ10= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ10.filll("black")
circ10.Drw(win)

circ11= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ11.filll("black")
circ11.Drw(win)

circ12= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ12.filll("black")
circ12.Drw(win)

circ13= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ13.filll("black")
circ13.Drw(win)

circ14= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ14.filll("black")
circ14.Drw(win)

circ15= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ15.filll("black")
circ15.Drw(win)

circ16= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ16.filll("black")
circ16.Drw(win)

circ17= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ17.filll("black")
circ17.Drw(win)

circ18= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ18.filll("black")
circ18.Drw(win)

circ19= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ19.filll("black")
circ19.Drw(win)

circ20= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ20.filll("black")
circ20.Drw(win)

circ21= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ21.filll("black")
circ21.Drw(win)

circ22= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ22.filll("black")
circ22.Drw(win)

circ23= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ23.filll("black")
circ23.Drw(win)

circ24= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ24.filll("black")
circ24.Drw(win)

circ25= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ25.filll("black")
circ25.Drw(win)

circ26= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ26.filll("black")
circ26.Drw(win)

circ27= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ27.filll("black")
circ27.Drw(win)

circ28= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ28.filll("black")
circ28.Drw(win)

circ29= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ29.filll("black")
circ29.Drw(win)

circ30= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ30.filll("black")
circ30.Drw(win)

circ31= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ31.filll("black")
circ31.Drw(win)

circ32= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ32.filll("black")
circ32.Drw(win)

circ33= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ33.filll("black")
circ33.Drw(win)

circ34= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ34.filll("black")
circ34.Drw(win)

circ35= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ35.filll("black")
circ35.Drw(win)

circ36= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ36.filll("black")
circ36.Drw(win)

'''
circ37= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ37.filll("black")
circ37.Drw(win)

circ38= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ38.filll("black")
circ38.Drw(win)

circ39= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ39.filll("black")
circ39.Drw(win)

circ40= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ40.filll("black")
circ40.Drw(win)

circ41= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ41.filll("black")
circ41.Drw(win)

circ42= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ42.filll("black")
circ42.Drw(win)

circ43= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ43.filll("black")
circ43.Drw(win)

circ44= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ44.filll("black")
circ44.Drw(win)

circ45= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ45.filll("black")
circ45.Drw(win)

circ46= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ46.filll("black")
circ46.Drw(win)

circ47= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ47.filll("black")
circ47.Drw(win)

circ48= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ48.filll("black")
circ48.Drw(win)

circ49= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ49.filll("black")
circ49.Drw(win)

circ50= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ50.filll("black")
circ50.Drw(win)

circ51= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ51.filll("black")
circ51.Drw(win)

circ52= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ52.filll("black")
circ52.Drw(win)

circ53= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ53.filll("black")
circ53.Drw(win)

circ54= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ54.filll("black")
circ54.Drw(win)

circ55= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ55.filll("black")
circ55.Drw(win)

circ56= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ56.filll("black")
circ56.Drw(win)

circ57= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ57.filll("black")
circ57.Drw(win)

circ58= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ58.filll("black")
circ58.Drw(win)

circ59= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ59.filll("black")
circ59.Drw(win)

circ60= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ60.filll("black")
circ60.Drw(win)


circ61= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ61.filll("black")
circ61.Drw(win)

circ62= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ62.filll("black")
circ62.Drw(win)

circ63= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ63.filll("black")
circ63.Drw(win)

circ64= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ64.filll("black")
circ64.Drw(win)

circ65= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ65.filll("black")
circ65.Drw(win)

circ66= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ66.filll("black")
circ66.Drw(win)

circ67= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ67.filll("black")
circ67.Drw(win)

circ68= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ68.filll("black")
circ68.Drw(win)

circ69= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ69.filll("black")
circ69.Drw(win)

circ70= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ70.filll("black")
circ70.Drw(win)

circ71= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ71.filll("black")
circ71.Drw(win)

circ72= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ72.filll("black")
circ72.Drw(win)

circ73= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ73.filll("black")
circ73.Drw(win)

circ74= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ74.filll("black")
circ74.Drw(win)

circ75= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ75.filll("black")
circ75.Drw(win)

circ76= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ76.filll("black")
circ76.Drw(win)

circ77= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ77.filll("black")
circ77.Drw(win)

circ78= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ78.filll("black")
circ78.Drw(win)

circ79= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ79.filll("black")
circ79.Drw(win)

circ80= Particle(random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.choice([-1,1])*random.uniform(-math.sqrt(vel),math.sqrt(vel)),random.randint(3,297),random.randint(3,297),r)
circ80.filll("black")
circ80.Drw(win)
'''




shapes = [circ1,circ2,circ3,circ4,circ5,circ6,circ7,circ8,circ9,circ10,circ11,circ12,circ13,circ14,circ15,circ16,circ17,circ18,
circ19,circ20,circ21,circ22,circ23,circ24,circ25,circ26,circ27,circ28,circ29,circ30,circ31,circ32,circ33,circ34,circ35,circ36]

'''
circ36,
circ37,circ38,circ39,circ40,circ41,circ42,circ43,circ44,circ45,circ46,circ47,circ48,circ49,circ50,circ51,circ52,circ53,circ54,
circ55,circ56,circ57,circ58,circ59,circ60,circ61,circ62,circ63,circ64,circ65,circ66,circ67,circ68,circ69,circ70,circ71,circ72,
circ73,circ74,circ75,circ76,circ77,circ78,circ79,circ80]
'''





while True:
    moveAll(shapes)
    checkSides(shapes,win)
    checkCollisions(shapes)
    dt = datetime.now()
    dt.microsecond
    RMS = getRms(shapes)
    print(RMS , "<------>" , getTemperature(shapes,RMS),"<----->",dt)
    #time.sleep(.01)
