#Works cited
# Code modified from https://www.derekshidler.com/how-to-create-a-text-based-adventure-and-quiz-game-in-python/
# https://www.programiz.com/python-programming/global-keyword

#imports time module to provide a delay in response.
import time


#attempts to control for all possibilities in user input.
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "Yes"]
no = ["N", "n", "no", "No"]
name = []


print('                                 A Night in Geisel!                           ')
print('------------------------------------------------------------------------------')
print('******************************************************************************')
print('------------------------------------------------------------------------------')


#Allows player name to be custom
def player_name():
    print('What is your name?')
    global name
    name= input()
    intro()
    
#Introduction level of game, prints story and sends player to what_now().
def intro():
    print(name+ """ Wakes up, it is pitch black....
The last thing """+name+""" remembers is studying for a final exam in Geisel Library....""")
    time.sleep(3)
    print("""After looking around it appears that """+name+""" is still on the 14th floor.
"""+name+""" shouts-- Hello! is anyone there??"""
""" There is no response, it appears as though you are entirely alone...
What should """+name+""" do?""")
    time.sleep(3)
    what_now()
    
# Gives players 3 options for what to do next.
def what_now():
    print("""A - Go to the elevator.
B - Go to the stairs.
C - Go back to sleep.""")
    choice = input(">>> ")
    if choice in answer_A:
        option_elevator()
    elif choice in answer_B:
        option_stairs()
    elif choice in answer_C:
        option_sleep()
    else: 
        print('Choice Required: A,B,C')
        intro()

#returns player what_now()
def option_elevator():
    time.sleep(1)
    print(name + " goes to the elevator, but it does not appear to be working, they wait and wait but it never comes.")
    time.sleep(4)
    print(".....Crap! What is " + name + " going to do now??")
    what_now()
    
#Prompts players to go down the stairs giving them 2 choices
    #at this point the choices are irrelevent.
def option_stairs():
    time.sleep(1)
    print(name + """ goes to the stairwell and opens the door, but it is extremely dark inside.
Should they use their phone for light?
Yes or No?""")
    choice = input(">>> ")
    if choice in yes:
        print(name + " pulls out an iPhone and starts down the stairs.")
        down_stairs()
    elif choice in no:
        print(name + " starts down the stairs in the darkness......I hope they have great nightvision.....")
        down_stairs()
    else:
        print('Choice Required: Yes or No')
        option_stairs()

# 3 potential paths
    #A- takes player down stairs
        #Death from walking or from running
    #B- Death
    #C- Returns to what_now()
    
def down_stairs():
    time.sleep(2)
    print("""As """+ name + """ walks down, floor after floor, they begin to smell a musty odor and hear footsteps coming closer.
A faint whisper on the air appears to say  """+ name +'....'+name+'.....' """ in a way that sends chills up their spine"""
"""
What should they do?
A - Continue walking carefully
B - Run!
C - Go back to the 14th floor.""")
          
    choice= input(">>>")
          
    if choice in answer_A:
        print(name + """ continues down the stairs but the footsteps are still getting closer, and they begin to hear heavy breathing.
The fear is crippling!
Should they run now?
Yes or No?""")
        choice = input(">>>")
        if choice in yes:
        
            print(name + """ started running down the stairs as fast as their legs would cary them!
As they finally reached the 1st floor they tripped on the last stair and hitting their head as they fell """
+ name + """ DIED!!!

------------------------------------------------------------------------------
*****************************GAME OVER!!!*************************************
------------------------------------------------------------------------------

""")
        elif choice in no:
            print("""They continue to walk slowly even though they are terrified.....
SUDDENLY SOMETHING GRABS """ +name+""" FROM BEHIND!!! 
"""+ name + """ DIED!!!

------------------------------------------------------------------------------
*****************************GAME OVER!!!*************************************
------------------------------------------------------------------------------

""")
        else:
            print('Choice Required: Yes or No')
            down_stairs()
    elif choice in answer_B:
        print(name + """ started running down the stairs as fast as their legs would cary them!
As they finally reached the 1st floor they tripped on the last stair and hitting their head as they fell """
+ name + """ DIED!!!



------------------------------------------------------------------------------
*****************************GAME OVER!!!*************************************
------------------------------------------------------------------------------

                                
""")
    elif choice in answer_C:
        print(name + """ runs up the stairs as fast as their legs would carry them!
Whew! they reached the 14th floor!""")
        what_now()
          
#sleep the only way to win the game                   
def option_sleep():
    print(name + """ wakes up a few hours later to a tap on the shoulder. 
As they open their eyes they notice that the sun is shining.
An angry security guard ask's """+ name +""" how they got in here before rudely kicking them out!


------------------------------------------------------------------------------
***************************** CONGRATULATIONS!!!!!! **************************
------------------------------------------------------------------------------
------------------------------------------------------------------------------
*************************** """ +name+ """ SURVIVED THE NIGHT!!!!! ********************
------------------------------------------------------------------------------
""")
    
player_name()