import RPi.GPIO as IO
import time                    #calling time to provide delays in program
IO.setwarnings(False)          #do not show any warning
IO.setmode(IO.BCM)

#defining line  which signal is of base frequencu
inC = 22 #i.e. GPIO 22
#defining line  which will control doubling of frequency
inD = 17 #i.e. GPIO 17
#defining line for end of the program
inE = 4  #i.e. GPIO 4
#defining the pair of lines for output
outA = 6 #i.e. GPIO 6
outB = 19 #i.e. GPIO 19

IO.setup(outA,IO.OUT)           # initialize outA as an output.
IO.setup(outB,IO.OUT)           # initialize outB as an output.
IO.setup(inC,IO.IN)             # initialize inC as input.
IO.setup(inD,IO.IN)             # initialize inD as input.
IO.setup(inE,IO.IN)             # initialize inE as input.

A_pwm = IO.PWM(outA,100)          #outA as PWM output, with 100Hz frequency
B_pwm = IO.PWM(outB,100)          #outB as PWM output, with 100Hz frequency
c = IO.input(inC)   			  #c is input from line inC
d = IO.input(inD)   			  #d is input from line inD
e = IO.input(inE) 				  #e is input from line inE

A_pwm.start(50)                    #generate PWM signal with 50% duty cycle
B_pwm.start(50)                    #generate PWM signal with 50% duty cycle

while 1:
	c = IO.input(inC)       # read status of pin/port and assign to variable c
	d = IO.input(inD)       # read status of pin/port and assign to variable c
	e = IO.input(inE)       # read status of pin/port and assign to variable e
	#priority of inputs e>d>c
	if not e :
                #check for 5 seconds
                start = time.time()
                time.clock()            
                elapsed = 0.0
                flag = 0
                while elapsed < 5.0 :
                        time.sleep(0.5)   #sleep for 0.5 second
                        elapsed = elapsed+0.5
                        if c or d or e:
                                flag = 1
                                break
                if flag:			  #till 5 seconds not all 3 lines were lo
                        continue
                else:
                        A_pwm.stop()
                        B_pwm.stop()
                        break 
	elif d :
		A_pwm = IO.PWM(outA,200)	#start both PWM with 200Hz
		B_pwm = IO.PWM(outB,200)	#start both PWM with 200Hz
	elif not c :
		A_pwm = IO.PWM(outA,100)	#start both PWM with 100Hz
		B_pwm = IO.PWM(outB,100) 
	else :
		continue #no_change

IO.cleanup()          # when your program exits, tidy up after yourself 
