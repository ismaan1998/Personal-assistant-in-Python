
from database import speech_recog_is_on
import speech_recog
import assistant_details
from output_module import output
def take_input():

    if speech_recog_is_on():
        data = speech_recog.listen_to_voice()
        if assistant_details.name in data:
           
            return data
            
    #command line input
    i = input("me: ")
    return i



