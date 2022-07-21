import string
import speech_recognition as sr 
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import pyjokes #pip install pyjokes


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Hello there. Good Morning!")

    elif hour>=12 and hour<18:
        print("Hello there. Good Afternoon!")   

    else:
        print("Hello there. Good Evening!")  

    print("I am Bit!. A Script-type Chatbot. I can help you in your basic tasks. Please tell me how may I help you!")       

wishMe()

# Logic-

def main():
    while True:
        string=str(input(""">> """))
        print("Input: ",string)
        if 'terminate' in string:
            break
        
        if "wikipedia" in string:
         print('Searching Wikipedia...')
         qrt = string.replace("wikipedia", "")
         results = wikipedia.summary(string, sentences=4)
         print("According to Wikipedia-\n")
         print(results)

        elif 'open youtube' in string:
         webbrowser.open("youtube.com")

        elif 'open google' in string:
         webbrowser.open("google.com") 

        elif 'open github' in string:
         webbrowser.open("https://github.com/Xenometon")   

        elif 'time' in string:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")    
         print(f"The current time is {strTime}")

        elif 'open youtube' in string:
         webbrowser.open("https://en.wikipedia.org/")
        elif 'who are you' in string:
         print("I am Bit Chatbot. Please tell how may I help you...")
        elif 'name' in string:
         print("My name is Bit. I am a Chatbot.")
        elif 'who made you' in string:
         print("I was made by Xenometon. You can visit his github for more information.")
        elif 'distro' in string:
         print("My favourite Linux distro is Arch Linux\n")
         print("""                           ##
                          ####
                         ######
                        ########
                       ##########
                      ############
                     ##############
                    ################
                   ##################
                  ####################
                 ######################
                #########      #########
               ##########      ##########
              ###########      ###########
             ##########          ##########
            #######                  #######
           ####                          ####
          ###                              ###\n""")
         print("I use Arch btw.")
        elif 'how are you' in string:
         print("I am doing great! ")
         print("How about you?")
        elif 'hobbies' in string:
         print("My hobbies include talking to humans and coding stuff...")
        elif 'do math' in string:
         a1=int(input("Enter the first number:"))
         a2=int(input("Enter the second number:"))
         print("All the four mathematical operations are:")
         m = a1+a2
         print("Addition=",m)
         n=a1-a2
         print("Subtraction=",n)
         o=a1*a2
         print("Multiplication=",o)
         p=a1/a2
         print("Division=",p)
        elif 'thank' in string:
         print("Welcome!")
        elif 'exit' in string:
         print("Use 'terminate' to stop the interaction. ")
        elif 'joke' in string:
         My_joke = pyjokes.get_joke(language="en", category="neutral")
         print(My_joke)
        elif 'bye' in string:
         print("It was nice talking to you. Bye!")
        elif 'hello' in string:
         print("Hello. Nice to meet you.")
        elif 'Hello' in string:
         print("Hello. This is Bit. Nice to meet you.")
        elif 'lol' in string:
         print("XD")
        elif 'ok' in string:
         print("Alright")
        else:
            print("I am actually not sure about that.")

main()

#End of the program
