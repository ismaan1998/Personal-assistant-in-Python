from input_module import take_input
from process_module import process
from output_module import output
import welcome
import os 
os.system("clear")

#welcome message
welcome.greet()

while(True):
    i = take_input()
    o = process(i)
    output(o)