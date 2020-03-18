from output_module import output
from time_module import get_time
from input_module import take_input
from database import get_answer_from_memory, insert_question_and_answer
from internet import check_internet_connection, check_on_wikipedia

def process(query):

    answer = get_answer_from_memory(query)

    if answer == "":
        answer = check_on_wikipedia(query)
        if answer != "":
            return answer



    if answer == "get time details":
        return ("Time is " + get_time())

    elif answer == "check internet connection":
        if check_internet_connection():
            return "internet is connected"
        else:
            return "internet is not connected"

    else:

        output("I don't know this one, can you please tell me what it means?")
        ans = take_input()
        if "it means" in ans:
            ans = ans.replace("it means", "")
            ans = ans.strip()

            value = get_answer_from_memory(ans)
            if value == "":
                return "Can't help with this one "
            
            else:
                insert_question_and_answer(query, value)
                return "Thanks i will remember it for the next time"
        
        else:
            return "can't help with this one"
        