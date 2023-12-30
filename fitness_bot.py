import openai
import pyttsx3


openai.api_key = "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"


def speak_text(text):

 engine = pyttsx3.init()
 engine.say(text)
 engine.runAndWait()


#user input
def fitness_bot(user_message,user_role):


     #create prompt, it pass user input with sentence
    prompt = f"as a {user_role}, i want to know more about {user_message}"


    response = openai.Completion.create(
                   engine = "text-davinci-002" ,         #it is a textmodel- advanced models may reduce the credits we have, so we use medium one
                   prompt = prompt,
                   max_tokens = 150 #length of response
        
    )
    bot_message = response['choices'][0]['text'].strip()

    return bot_message


#user_role = "fitness_trainer"
#user_message = "diet plan for 3 months"

#print(fitness_bot(user_message=user_message,user_role=user_role))



    
user_role = input("Please specify your role: ")

 
while True:
    
    
    user_input = input("Message: ")

    if user_input.lower() in ['bye','exit','quit']:
        break
    bot_response = fitness_bot(user_input,user_role)
    print(bot_response)
    speak_text(bot_response)

