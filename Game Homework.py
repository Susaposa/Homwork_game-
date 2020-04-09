phone_call = 3
has_key = True
def living_room():
  
  
  print('You are in the living room')
  print('east: go to the cellar')
  print('south: go to the kitchen')
  answer = input('?')
  if answer == 'south':
    kitchen()
  elif answer == 'east':
    cellar()
  else:
    living_room()
  # print

def study():
  global has_key
  if has_key == True:
    choice = input('You find a key. Do you want to put it in your pocket?')
    if choice == 'yes':
      print('The key is now in your pocket')
    else:
      print('You leave the key where it is and move to the next room.')
    

  print('You are in the study')
  print('west: go to the living room')
  print('north: go to the kitchen')
  answer = input('?')
  if answer == 'west':
    living_room()
  elif answer == 'north':
    kitchen()
  else:
    study()


def cellar():
  print('Now you are in the cellar. It is very dusty and there are a few spiders')
  print('Phone rings. Yes, IN THE CELLAR. Do you answer it?')
  phone_call = input('?')
  if phone_call == 'yes':
    print('You answered the phone. You must go to the study')
    study()
  else:
    print('You did not answer. You now have to decide where to go next')
    print('east: go to the garden')
    print('west: go to the kitchen')
    answer = input('?')
    if answer == 'east':
      garden()
    elif answer == 'west':
      kitchen()
    else:
      living_room()
 

def bathroom():
  print('You have ended up in the bathroom. You have two options, either go back to the living or go to the kitchen, because you are feeling peckish')
  print('north: go to the living room')
  print('west: go to the kitchen')
  answer = input('?')
  if answer == 'north':
    study()
  elif answer == 'west':
    kitchen()
  else:
    bathroom()



def garden():
  print('It is sunny outside and you decide to go to the garden for a stroll. But you get bored quickly and want to change locations.')
  print('north: go to the study')
  print('west: go to the bathroom')
  answer = input('?')
  if answer == 'north':
    study()
  elif answer == 'west':
    kitchen()
  else:
    garden()

def garage():
  print('Suddenly you need to go for a drive.')
  print('north: go to the living room')
  print('west: go to the kitchen')
  answer = input('?')
  if answer == 'north':
    study()
  elif answer == 'west':
    kitchen()
  else:
    bathroom()





def kitchen():

  print('You are in the kitchen')
  print('The pantry is locked. Do you have the key?')
  has_key = input('?')
  if has_key == 'yes':
    print('Good, you have opened the pantry. Now make me a sandwich')
  else: 
    print('Go back to the living room and start over')
    living_room()
  

living_room()


# print('Hello, welcome to my game')


# def play_game():
#     score = 0
    

#     answer = input('Are you ready to play?')
#     if answer == 'yes':
#         score += 1
#         answer = input('How much are you in love with Susana? A lot or a little?')
#         if answer == 'a lot':
#             score += 1
#             print('Awww...She loves you too')
#         else:
#             print('Well, fuck you then!')
        
#         print('Game completed!')
# play_game()









