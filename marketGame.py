# This Game was created by The Bwengo Man on 24th -> 25th of April 2022
# In this game you are given money by your parents to go to the market to buy something

# 1. You have to reach their in time
# 2. You have to stay healthy
# 3. You have to have enough money to buy the goods by the time you reach your destination
"""To play the game you'll be prompted with a text input like the one 
below and you'll have to enter an option 

press the 'Ok' or 'Cancel button to continue...
"""
from random import randint, randrange
from time import gmtime
from turtle import *

player = Turtle() #player object
dest = Turtle() #destination object
title("This Game") #Game title

play_game = True
start_game = False
destination = ['market', 'mall', 'shop', 'streets']

# game instructions 
textinput("Greetings am a guide please read me!", "This Game was created by The Bwengo Man on 24th -> 25th of April 2022\n\nIn this game you are given money by someone to go to the market to buy something\n\n1. You have to reach their in time\n2. You have to stay healthy\n3. You have to have enough money to buy the goods by the time you reach your destination\n\nTo play the game you'll be prompted with a text input like the one\nbelow and you'll have to enter an option\n\npress the 'Ok' or 'Cancel button to continue...")
# task givers 
double_title = [ 'Uncle', 'Auntie', 'Big Bro', "Lil Sis", "Some Random Guy", 'Grand Dad', 'Grand Ma',"Big Sis", "Lil Bro", 'Sister', 'Cousin']

single_title = ['Mother', 'Father', "Bwengo Man",'Grand Dad', 'Grand Ma',"Big Sis", "Lil Bro", 'Sister', 'Cousin', 'Uncle', 'Auntie', 'Big Bro', "Lil Sis", "Some Random Guy" ]
males = ['Banda', 'John', 'Nathan', 'Edward', 'Ishmael', 'Iqram', 'Sam', 'Farid', 'Joe', "Patrick", "Japhet", "David"]
females = ["Catherine", 'Justina', 'Patience', "Shamira", "Esther", "Maria", "Mumu", "Nakazwe", "Sarah", "Rosemary", "Mary"]

comodities = ['milk', 'bread', 'butter', 'mealie meal', 'water', 'shoes', 'chocolate', 'juice', 'lemons', 'avocados', 'fries', 'roasted chicken', 'beef', 'tango pina']


# Game loop 
while play_game:

    # game variables 
    hunger = 0
    money = 0
    thirst = 0
    time_remaining = randint(20, 60)

    walk_distance = 0
    distance = randrange(100, 250)
    task_giver = None
    name_of_TM = None
    money = randint(100, 150)
    price = money - 60

    # game canvas 
    bgColors = ['black', 'white']
    bcolour = bgColors[randint(0, (len(bgColors)-1)) ]
    bgcolor(bcolour)

    # creating the player object 
    player.shape('turtle')
    player_colors = ['cyan', 'blue', 'white', 'red', 'yellow', 'green', 'teal', 'purple', 'orange', 'grey', 'brown', 'black']

    destShape = ['circle', 'square', 'triangle', 'classic']
    dest.shape(destShape[randint(0, len(destShape)-1)])
    dest.shapesize(5)
    # player color selection 
    matched_colors = True
    count = 0
    while matched_colors: #Making sure that the player, destination and the background colours never match
        
        pcolour = player_colors[randint(0, (len(player_colors)-1))]
        dcolour = player_colors[randint(0, (len(player_colors)-1))]
        
        if pcolour != bcolour and bcolour != dcolour and bcolour != pcolour:
            player.color(pcolour)
            dest.color(dcolour)
            matched_colors= False
    

    player.setpos(-330,-100)
    player.clear()

    dest.setpos(distance, -100)
    dest.clear()


    # creating a destination
    place_to_go = destination[randrange(0, (len(destination)-1))] #Selecting a random destination
    
    #selecting stuff to be bought
    stuff_to_buy = comodities[randint(0, (len(comodities)-1))]

    #Creating task giver logic
    task_giver_type = randint(0, 1)

    if task_giver_type == 0:
        task_giver = single_title[randint(0, (len(single_title)-1))]

        if task_giver == "Bwengo Man":
            # task_giver = single_title[randint(0, (len(single_title)-1))]
            task_giver = task_giver
           
        else:
            task_giver = 'your ' + single_title[randint(0, (len(single_title)-1))]

    else:
        gender = randint(0, 1)
        if gender == 0:
            name_of_TM = males[randint(0, (len(males)-1))]
        else:
            name_of_TM = females[randint(0, (len(females)-1))]

        task_giver = 'your ' + double_title[randint(0, (len(double_title)-1))] + " "+ name_of_TM
    
    # input(f'\nYou have been told to go to the {place_to_go} by {task_giver} to buy {stuff_to_buy}\nthe {stuff_to_buy} cost k{price} and you have been given an amount of k{money}\nyour mission is to reach the {place_to_go} before they close in {time_remaining} minutes\nbuy whatever you have been tasked to buy \nthe distance to the {place_to_go} is {distance}m\n\npress enter to continue...')
    textinput("Just some stuff",f'\nYou have been told to go to the {place_to_go} by {task_giver} to buy {stuff_to_buy}\nthe {stuff_to_buy} cost k{price} and you have been given an amount of k{money}\nyour mission is to reach the {place_to_go} before they close in {time_remaining} minutes\nbuy whatever you have been tasked to buy \nthe distance to the {place_to_go} is {distance}m\n\npress enter to continue...')
    # text("You are the man", 13)
    # Turtle().write(f'\nYou have been told to go to the {place_to_go} by {task_giver} to buy {stuff_to_buy}\nthe {stuff_to_buy} cost k{price} and you have been given an amount of k{money}\nyour mission is to reach the {place_to_go} before they close in {time_remaining} minutes\nbuy whatever you have been tasked to buy \nthe distance to the {place_to_go} is {distance}m\n\npress enter to continue...',False, 'center', 'arial')
    # game logic 


    start_game = True
    count = 0
    food_water_price = 0
    move_dis = 0
    dmove_control = 250
    while start_game:
        if count <3:
            food_water_price = int(money*0.1)
        else:
            food_water_price = int(money*0.25)
    #user input
        # user_choice = input(f"\n1. Walk focused to the {place_to_go}\n2. Walk and think\n3. Run\n4. buy food and water at k{food_water_price}\nenter choice to proceed :")
        user_choice = textinput("Enter Your Choice?", f"\n1. Walk focused to the {place_to_go}\n2. Walk and think\n3. Run\n4. buy food and water at k{food_water_price}\n\n5. Restart game\n6. Quit game\nleave blank to check status but with consequences\n\nenter choice to proceed :")

    # input("check")
        if user_choice == '1':
            move_dis = int(distance*0.2)
            walk_distance += move_dis
            time_remaining -= int(time_remaining*0.2)
            thirst += int(0.3*100)
            hunger += int(0.1*100)
            player.fd(move_dis + (dmove_control*0.2))


        # Player walks and think 
        elif user_choice == '2':
            move_dis = int(distance*0.1)
            walk_distance += move_dis
            time_remaining -= int(time_remaining*0.36)
            thirst += int(0.15*100)
            hunger += int(0.26*100)
            player.fd(move_dis + (dmove_control*0.1))


        # Player runs 
        elif user_choice == '3':
            move_dis = int(distance*0.4)
            walk_distance += move_dis
            time_remaining -= int(time_remaining*0.1)
            thirst += int(0.65*100)
            hunger += int(0.06*100)
            player.fd(move_dis + (dmove_control*0.4))

        
        # Player buys stuff 
        elif user_choice == '4':
            move_dis = int(distance*0.01)
            walk_distance += move_dis
            time_remaining -= int(time_remaining*0.46)
            thirst -= int(0.50*100)
            hunger -= int(0.3 * 100)
            money -= food_water_price
            player.fd(move_dis + (dmove_control*0.1))


        # Restarting the game 
        elif user_choice == '5':
            start_game = False
            break

        # Quiting the game 
        elif user_choice == '6':
            start_game = False
            play_game = False
            break

        #else:
         #   textinput("Status summary", f"\nYou have moved {walk_distance}m out of {distance}m\nthe time remaining is {time_remaining} minutes\nyou are {thirst}% thirsty\nyou are {hunger}% hungry\nyour money balance is k{money}\nthe price of {stuff_to_buy} is k{price}\n\npress enter to continue...")

        # destructions
        met_friend = randint(0, 5)
        received_cash = randint(0, 10)
        got_lift = randint(0, 5)

        #Bringing randome destractions to the player some are good and some are bad
        if met_friend == randint(0, 5):
            chat_time = int(((randint(10, 50))/100)*time_remaining)
            move_dis = int(distance*0.01)
            walk_distance += move_dis
            time_remaining -= chat_time
            thirst += int(0.2*100)
            hunger += int(0.3 * 100)
            textinput("Met a friend", f"\nYou have met with your friend!!!\nand you have chat for {chat_time} minutes \n\npress enter to continue....")
            player.fd(move_dis + (dmove_control*0.01))

        # player gets a lift 
        elif got_lift == randint(0, 10):
            move_dis = int(distance*0.15)
            walk_distance += move_dis
            time_remaining -= int(time_remaining*0.05)
            thirst += int(0.06*100)
            hunger += int(0.03 * 100)
            textinput("Yey You got a lift!!!",f"\nYou have gotten a lift!!!\n\npress enter to continue....")
            player.fd(move_dis + (dmove_control*0.15))

        # player receives cash 
        elif received_cash == randint(0, 7):
            cash = randint(20, 50)
            money += cash
            textinput("Yey!!! You received some cash!", f"\nYou have received k{cash} from your {single_title[randint(0, (len(single_title)-1))]}\nyou can spend it as you want\n\npress enter to continue....")


        # winning the game 
        if distance <= walk_distance:
            if money >= price:
                money -= price
                play_or_not = textinput("You won the game!!!", f"\nCongratulations you have reached the {place_to_go}\nand you have bought the {stuff_to_buy}\nyour remaining balance is k{money}\n\npress enter to play again or press 'q' to quit\n\nchoose an option to proceed :")
                
                if play_or_not == 'q':
                    print('\nThanks for playing "The Time I was sent...\n\nBye!!!"')
                    start_game = False
                    play_game = False
                    break
                else:
                    start_game = False
            else:
                play_or_not = textinput("You lost the game", f"\nMission failed!!!\n\nYou have reached the {place_to_go}\nbut you don't have enough money to buy {stuff_to_buy}\nbalance ==> k{money}\nprice ==> k{price}\n\npress enter to play again or press 'q' to quit\n\nchoose an option to proceed :")

                if play_or_not == 'q':
                    print('\nThanks for playing "The Time I was sent...\n\nBye!!!"')
                    start_game = False
                    play_game = False
                else:
                    start_game = False

        # Killing the player if their thirst exceeds 100%
        if thirst>=100:
            play_or_not = textinput("You are daid!!", f"\nYou died of thirst\npress enter to try again or press 'q' to exit :").lower()
            if play_or_not == 'q':
                print('\nThanks for playing "The Time I was sent...\n\nBye!!!"')
                start_game = False
                play_game = False
            else:
                start_game = False
                
        # Killing the player if their hunger exceeds 100%
        elif hunger >=100:
            play_or_not = textinput("You died",f"\nYou died of hunger\npress enter to try again or press 'q' to exit :").lower()
            if play_or_not == 'q':
                print('\nThanks for playing "The Time I was sent...\n\nBye!!!"')
                start_game = False
                play_game = False
            else:
                start_game = False

        # game over if the player runs out of time
        elif time_remaining <= 0:
            play_or_not = textinput("Time up champ", f"\nYou run out of time\npress enter to try again or press 'q' to exit :").lower()
            if play_or_not == 'q':
                print('\nThanks for playing "The Time I was sent...\n\nBye!!!"')
                start_game = False
                play_game = False
            else:
                start_game = False

        else:
            textinput("Status summary", f"\nYou have moved {walk_distance}m out of {distance}m\nthe time remaining is {time_remaining} minutes\nyou are {thirst}% thirsty\nyou are {hunger}% hungry\nyour money balance is k{money}\nthe price of {stuff_to_buy} is k{price}\n\npress enter to continue...")
        count+=1 # print(task_giver)

        just_some_random_code_to_piss_off_the_editor_lol = "And it doesn't do anything lol wow what a variable name Bwengo man lol"
        here_I_got_bored_and_thought_why_dont_I_make_my_thoughts_a_variable_name_and_assign_it_to_nothing_lol=None