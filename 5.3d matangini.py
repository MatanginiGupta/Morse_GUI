# Matangini Gupta
# 22109948810
# TASK 5.3D Embedded systems

from tkinter import*  # Import the necessary libraries, including tkinter for GUI.
import tkinter.font  # Import tkinter font module.
from tkinter import ttk
from gpiozero import LED  # Import LED control from gpiozero.
import RPi.GPIO  # Import RPi.GPIO module for Raspberry Pi GPIO control.
RPi.GPIO.setmode(RPi.GPIO.BCM)  # Set GPIO mode to BCM for pin numbering.
import time  # Import the time module for time-related functions.

myLed = LED(18)  # Initialize an LED object for GPIO pin 18.
win = Tk()  # Create a Tkinter window.
win.title("BLINKING LED")  # Set the window title.

def BlinkLed(Input):
    for letter in Input:  # Iterate through the user input.
        if letter == 'a':
            dot()
            dash()
        elif letter == 'b':
            dash()
            dot()
            dot()
            dot()
        elif (letter=='c'):
            dash();
            dot();
            dash();
            dot();
        elif (letter=='d'):
            dash()
            dot()
            dot()
        elif (letter=='e'):
            dot()
        elif (letter=='f'):
            dot()
            dot()
            dash()
            dot()
        elif (letter=='g'):
            dash()
            dash()
            dot()
        elif (letter=='h'):
            dot()
            dot()
            dot()
            dot()
        elif (letter=='i'):
            dot()
            dot()
        elif (letter=='j'):
            dot()
            dash()
            dash()
            dash()
        elif (letter=='k'):
            dash()
            dot()
            dash()
        elif (letter=='l'):
            dot()
            dash()
            dot()
            dot()
        elif (letter=='m'):
            dash()
            dash()
        elif (letter=='n'):
            dash()
            dot()
        elif (letter=='o'):
            dash()
            dash()
            dash()
        elif (letter=='p'):
            dot()
            dash()
            dash()
            dot()
        elif (letter=='q'):
            dash()
            dash()
            dot()
            dash()
        elif (letter=='r'):
            dot()
            dash()
            dot()
        elif (letter=='s'):
            dot()
            dot()
            dot()
        elif (letter=='t'):
            dot()
            dot()
            dot()
            dot()
        elif (letter=='u'):
            dot()
            dot()
            dash()
        elif (letter=='v'):
            dot()
            dot()
            dot()
            dash()
        elif (letter=='w'):
            dot()
            dash()
            dash()
        elif (letter=='x'):
            dash()
            dot()
            dot()
            dash()
        elif (letter=='y'):
            dash()
            dot()
            dash()
            dash()
        elif (letter=='z'):
            dash()
            dash()
            dot()
            
# Function to represent a dash in Morse code.
def dash():
    myLed.on()
    time.sleep(0.8)
    myLed.off()
    time.sleep(0.2)

# Function to represent a dot in Morse code.
def dot():
    myLed.on()
    time.sleep(0.2)
    myLed.off()
    time.sleep(0.2)
    
def morse_box():
    input = box.get("1.0", "end-1c")  # Get user input from the text widget.
    BlinkLed(input)  # Call the function to display Morse code for the input.

# A label with instructions for the user.
l1 = Label(win, text='NOTE: Limit of max 12 characters', font=('Arial', 12))
l1.pack()

# A custom frame with a double border for the text box.
frame = ttk.Frame(win, borderwidth=2, relief="groove", padding=5)
frame.pack()

box = Text(frame, height=2, width=25, bg="grey", fg="white")
box.pack()

# A custom frame with a double border for the button.
button_frame = ttk.Frame(win, borderwidth=2, relief="groove", padding=5)
button_frame.pack()

# A button that triggers the Morse code display.
enter = Button(button_frame, text="Signal!", command=morse_box, bg='Blue', height=2, width=20)
enter.pack()

# Increase the heading size to fit on the banner.
heading_font = tkinter.font.Font(family='Arial', size=25, weight='bold')
heading = Label(win, text='MORSE CODE TRANSLATOR', font=heading_font)
heading.pack()

win.mainloop() # Start the main loop to run the GUI and wait for user input.
