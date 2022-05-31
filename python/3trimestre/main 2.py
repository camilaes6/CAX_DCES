print("hi welcome to tresure scape")
name=(input("type in your username: "))
print("welcome",name)

print("in this game your going to travel to the deep ocean wirh pancho the fish to live different adventures with him, he is a clown fish, who's orange with vlack and white, his personality is super funny, positive and has always the best vibes")

print("your also going to find perlita, she's also a fish, a Blue Hippo Tang actually, her personality is super diva, sassy and fashion")

print(" there's also chiqui the turtle who is a turtle, he is hippie and always calm, happy, peaceful and supportive with everyone around him")

character1="chiqui the turtle" 
character2="perlita"
character3="pancho the fish"

characterpick=int(input("what character are you choosing today: "))

print("perfect, great choice!")

if(characterpick==1):
  print("chiqui: welcome to my world, i am glad to have you here! are you ready to start? ")
  input()
  print("i have 4 adventures for today, can you help me? a/b/c/d")

  desicion=input()

  if desicion=="a":
    print("today we're going to cook avo toast")
    print("nice, come with me to the fridge so we can get the ingredients")
    print("would you like a fried egg on yours")
    input()

    egg=input("yes or no: ")
    if (egg=="yes"):
      print("let's cook it!")
      print("how do you like the yolk?")
      yolk=input("cooked or raw: ")
      if (yolk=="cooked"):
        print("nice lets leave it cooking in the pan for aprox 8 mins")
      elif (yolk=="raw"):
        print("okie! it will take only 4 minutes in the pan")

    elif (egg=="no"):
      print("thats ok lets proceed with the rest")

    print("well while the egg is ready lets start with the rest :) ")
    print("what type of bread do you eat?")
    bread=input("normal or light")
    answer=input()
    if (answer=="normal"):
      print("ooo i like that one lets get it and well be ready to toast it")
    else:
      print("lets get it and well toast it")

      print("well now that you've choosed your type of bread, lets choose in what level of toasting do you like ")

      print("what toast level are you choosing? 1/3/5: ")

    level=input()
    
    if (level==1):
      print("great it'll be ready in 30s")

    elif (level==3):
      print("okie! it will be ready in 1min")

    else:
      print("nice it will be ready in 1 min and 30s")

      print("alright now that your bread is ready lets put the avocado on it")

    avocado=input()
    print("would you likeyour avocado mashed or in cubes?")

    if (avocado==mashed):
      print("alright lets mash!!")
      print("grab a bowl and a fork to begin")
      print("nice your avocado is now perfectly mashed")

    else:
      print("nice lets chop chop chop")
      print("so lets take our knife and a plate and we can begin the chopping ")
      print("oooh those cubes are perfect")

    print("we are almost ready now its just time that we ensable all the pieces")
    print("lets begin")
    print("but let me explain you, this part is like a puzzle but here in my world avo toasts are not as in yours")
    print("so this beautiful avotoast machine is going to tell you how to do it ")
    import random 
    avo=("bread, avo,egg", "egg,bread,avo", "avo, egg,bread")
    print(random.choice(avo))

    print("perfect, we've finished i can't believe this cooking adventure is over enjoy your avotoast!")

    print("thank you so much for being here with me, see you soon")

    
       
  elif desicion=="b":
     print("we are going to go on a trip with my dolphin friends to twinky island")
     print("ready for the trip?")
     input()
     print("we're leaving now, first we're taking the sea train and then a 2 hour roadtrip to the island")
     print("nice we arrived to the train station, lets buy our tickets")
     print("ticket seller: hi! welcome to the sea train station were are you going today? ")
     input()
     print("ticket seller: nice that island is beatiful, 2 tickets right? ")
     input()
     print("ticket seller: great, the trains that go there are scheduled for: a) 3pm, b) 6:20pm and c) 10 pm, wich one would you like? ")
     ticket=input()

     if (ticket=="a"):
       print("perfect! you have 10 minutes to board the train, your gate is 10A. Nice trip!!")
       print("chiqui: alright now we better run to catch the train, we still have to pass security and then find our gate")
       print("oh my god we really had a sprint to get here, but we're finally on security")
       
     elif (ticket=="b"):
       print("ok! you have 2 hours to board the train, your gate is 12C. Have a nice trip!")

     else:
       print("nice! you have 4 hours to board, your gate will be 3K. Enjoy your trip!!")

     print("police guard: hi welcome to security please put your stuff in the band so we can check it ")
     print("if you have something over 100ml or dangerous stuff please put it out before we have to")
     print("ok, so please ")

     
    
    
    
    

  elif desicion=="c":
    print("now we're heading to my cousin tutu's house to have a swim race")
    print("youre going to love my cousin she's super funny and cool")
    print("grab your swimsuit and we'll be ready for the adventure!")
    print("to get to her house we have to walk but the road in over the water so you will also need to jump")
    print("just follow me!")
    print("lets start moving, but this road is tricky, you will have to do the opposite of what i say")
    print("for example, if i say left you'll need to move right or if i say up you'll have to go down")
    print("lets begin")
    right=input()
    print("right")
    if (right==right):
      print("left")
    

  else:
    print("were going to go on a trip to earth")






elif(characterpick==2):
 print("welcome to perlita's world")
 print("perlita: welcome to my world, i am glad to have you here! are you ready to start? ")
 input()
 print("today we have 2 types of    adventures 1/2")
 desicion=input()
 if desicion=="1":
     print("nice, today we'll have to open a treasure that i found many years ago")
     print("let me tell you the story behind it")
     print("100 years ago when i lived in the pacific ocean, me and my friends found this amazing treasure chest in a cave, but since then i have not been able to open it because it requires a password that i havent deciphered")

     print("luckily i have some clues about it, we know that:")
     print("it contains 4 numbers")
     print("so now that you're aware of all of this information")
     print("are you ready to hop in this adventure?")
     input()
     print("lets start, if we can decipher it on 4 tries you can get half of whats inside")

     for x in range(4):
      print("enter the password: ")
      password=int(input())

      if (password==4567):
        print("nice! you got it, im extremely greatful and happy with you, you got half of the treasure")
        break 

      else:
        print("umm its wrong, lets try again")
        print("this adventure has finished thank you so much for this, if you want more you can run agoin the code to find more adventures! see you later")

 else:
   print("hi welcome! today im offering you to be my dance partner in a dance competition so... would you be my partner?  ")
   partner=input()
   if (partner=="yes"):
     print("omg you just made me so happy but i'll be happier if we win the competition so lets put all of our efforts on it ")
     print("the dance hall is two blocks away so we can walk there and get ready")
     print("since i knew you were going to say yes i already asked for our customs but i want to know your clothing size so the company can deliver them asap")
     print("so what's your clothing size s/m/l?: ")
     size=input()
     if (size=="s"):
       print("alright i'll let them know so our customes will be ready")

     elif (size=="m"):
       print("nice! let me text the company so they deliver it now")

     else:
       print("great! ill call them so our customes are ready for the competition")

   print("omg were here and we have our customes lets wait for them to give us our participation number")

   import random 
  dancenum=("3", "7", "1", "4")
  print(random.choice(dancenum))

  print("ok we have it, i can't believe this is happening")
  print("are you nervous")
   nervous=input()
  if (nervous=="yes"):
     print("dont worry we'll do amazing")

  else:
    ("perfect thats amazing almost averyone here is nervous that makes us strenght")

  print("its our turn lets hope the judges behave nice with us haha")

  list=["salsa", "mambo", "regueton", "hiphop", "cumbia", "pop", "rock", "folklore"]

  dance1=random.choice[list]
  print(dance1)
  dance2=random.choice[list]
  print(dance2)
  dance3=random.choice[list]
   print(dance3)
   dance4=random.choice[list]
   print(dance4)
   dance5=random.choice[list]
   print(dance5)
   dance6=random.choice[list]
   print(dance6)
   dance7=random.choice[list]
   print(dance7)
   dance8=random.choice[list]
   print(dance8)

   1dance=input("dance1")
   2dance=input("dance2")
   3dance=input("dance3")
   4dance=input("dance4")
   5danche=input("dance5")
   6dance=input("dance6")
   7dance=input("dance7")
   8dance=input("dance8")

   
  if (dance1=1dance and dance6=6dance)
  elif(dance2=2dance and dance3=3dance)
   break

  else:
    print("you just lost the competition")
   
    

      
     




     
   else:
     print("well thats bad, but its ok i'll find another partner see ya!")
     print("game over")
      

elif (characterpick==3):
  print("welcome to pancho's world")
  print('pancho: welcome to my world, i am glad to have you here! are you ready for this adventure ? ')
  input()
  print('today i have to go to the supermarket before anything else ')
  print('would you like to come with me ?')
  input()
  print('awesome i wont take that long ')
  print('i just need some popcorns and cookies for a movie night that i wil be hosting in the night  ')
  print('would you like to come ? yes/no')
  desicion=input()

  if (desicion=="yes"):
    print("great")
    print('do you want to buy any specific candies for today night ?')
    candy=input("a)chocolate,b)gummy bears,c)chips")

  if (candy=="a"):
    print("what kind of chocolate dark or white?")

    chocolate=input()

    if (chocolate=="dark"):
      print("wow, thats a good one, not everybody likes it")

    else:  
     print('great option, i love that chocolate too ')

     if(candy=="b"): 
       print('would you like the spicy ones or the normal ones?')
       candy=input()

    if (candy=="spicy"):
      print("oooh you like things spicy")

    else:
      print("those ones are pretty good")
    
  else:
    print("i love chips, but would you like them of salt, spice or cheese")
    chips=input()

    if (chips=="salt"):
      print("those are good with some onion dip")
      print("would you like us to buy some dip, it doesnt need to be onion")
      desicion=input()
      if (desicion=="yes"):
        print("great! what type of dip would you like")
        print("the options that this supermarket offers are: a) american cheese b) onion")
        
        dip=input()
        if (dip=="a)"):
          print("yummy lets grab some")

        elif (dip=="b)"):
          print("great choice, grab some")

        print("great were now ready to pay since we have everything")

        print("lets pay in the self-checkout since it's easier")
        print("lets start scanning")
        print("great now its time to pay")
        print("lets use a card, what would you choose a) credit or b) debit?: ")

        card=input()
        if (card=="credit"):
          print("thats a great choice since you can accumulate points there from your purchases")

        else:
          print("perfect! that one's great to control your expences")

        print("im paying with my digital card since its safer")

        print("but since you know it gives a random number for the nip, but first lets enter all of the other data")

        print("card number: ")
        number=int(input())
        print("card holder: ")
        holder=int(input())
        print("expire date: ")
        date=int(input())

        import random 
        nip=("1234", "5678", "3901", "9012")
        print(random.choice(nip))

        print("well now we have everything and we can go home for the movie night")
        print("lets take a taxi to take us home")
        print("taxiii!")
        print("taxi driver: hi welcome aboard taxi 841 where do you want me to take you? ")
        destiny=int(input())
        print("taxi driver: perfect that would be aproximately $90.5")
        print("but let me tell you this taxi is magic anything could happen")
        print("but anyways, lets start your trip")
        import random
        car=("pum 💥holy moly we just crashed i think i was going to fast, unfortunately this makes me unable to take you to your destination, please find another transportation, ups", "woop the car just activated fly mode, thank god, now we can avoid all this traffic to get faster to your destination", "oh no! the car stopped working im sorry but you'll have to get down and find a new transportation")
        
       

        
        

      

        
        
        

      

