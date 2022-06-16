import machine
import utime
import _thread

#We connect the BUTTONS from the PINS
ButtonA = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
ButtonB = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)


# We connect the LEDS from the PINS
# Vehicle pins
RED = machine.Pin(10, machine.Pin.OUT)
YELLOW = machine.Pin(11, machine.Pin.OUT)
GREEN = machine.Pin(12, machine.Pin.OUT)

# Pedestrian pins
PEDESTRIAN_RED = machine.Pin(6, machine.Pin.OUT)
PEDESTRIAN_WAIT = machine.Pin(7, machine.Pin.OUT)
PEDESTRIAN_GREEN = machine.Pin(8, machine.Pin.OUT)

# Buzzer
Buzzer = machine.PWM(machine.Pin(15))
Buzzer.duty_u16(0)
Frequency = 1000

# Control variable
CrossRequested = False

# This function will be run on a separate thread representing the behaviour of the pedestrian
#semaphore when it is triggered
def PedestrianCross():
    global CrossRequested
    # We set the semaphore on green
    PEDESTRIAN_RED(0)
    PEDESTRIAN_GREEN(1)
    PEDESTRIAN_WAIT(0) # We close the light which signals that a pedestrian had requested to cross the street
    OnTime = 500
    print("Beeping")

    # We make the buzzer to beep
    for Beeping in range(10):
        Buzzer.duty_u16(32767)
        utime.sleep_ms(OnTime)
        print("Beep")
        Buzzer.duty_u16(0)
        utime.sleep_ms(1000-OnTime)
    print("End beep thread")

    # And we set the semaphore on red again
    PEDESTRIAN_RED(1)
    PEDESTRIAN_GREEN(0)
    CrossRequested = False

# Handler for the button
def ButtonIRQHandler(pin):
    global CrossRequested
    if CrossRequested == False:
        print("Button pressed")
        CrossRequested = True
        PEDESTRIAN_WAIT.value(1)

# Cleanup function to close all leds after the application is done
def stopAllLeds():
    RED.value(0)
    YELLOW.value(0)
    GREEN.value(0)

    PEDESTRIAN_RED.value(0)
    PEDESTRIAN_GREEN.value(0)
    PEDESTRIAN_WAIT.value(0)

# At the start of the program, we set both semaphore on red
def init_leds():
    RED.value(1)
    YELLOW.value(0)
    GREEN.value(0)

    PEDESTRIAN_RED.value(1)
    PEDESTRIAN_GREEN.value(0)
    PEDESTRIAN_WAIT.value(0)
    utime.sleep(2)
    
# The main function, it toggles the vehicles semaphore red to green and listens for a pedestrian to request a cross
def run():
    global CrossRequested
    init_leds()
    while True:
        if CrossRequested == True:
            _thread.start_new_thread(PedestrianCross, ())
            while CrossRequested:
                utime.sleep(1)
        else:
            YELLOW.value(1)
            utime.sleep(1)
            RED.value(0)
            YELLOW.value(0)
            
            GREEN.value(1)
            utime.sleep(2)
            YELLOW.value(1)
            GREEN.value(0)
            
            utime.sleep(1)
            RED.value(1)
            YELLOW.value(0)
            utime.sleep(2)

        
        
ButtonA.irq(trigger = machine.Pin.IRQ_RISING, handler = ButtonIRQHandler)
ButtonB.irq(trigger = machine.Pin.IRQ_RISING, handler = ButtonIRQHandler)


if __name__ == '__main__':
    run()
    stopAllLeds()
