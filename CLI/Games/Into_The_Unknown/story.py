class Quest:

    def __init__(self, player):
        self.player = player

    def get_location(self):
        location = str(input("Enter a location: \n\
                                    1. DARK ROOM\n\
                                    2. UNIMPLEMENTED\n\
                                    3. UNIMPLEMENTED\n\
                                    4. UNIMPLEMENTED\n")
                                )
        if location not in ["1", "2", "3", "4"]:
            print("Invalid choice")
            return(self.get_location())
        else:
            if location == "1":
                return "DARKROOM"
            elif location == "2":
                return "UNIMPLEMENTED"
            elif location == "3":
                return "UNIMPLEMENTED"
            elif location == "4":
                return "UNIMPLEMENTED"
    
    def story(self):

        if self.get_location() == "DARKROOM":

            while True:

                print("{} wakes up in a dark room.\n"
                "What should {} do?\n".format(self.player.name, self.player.name))
                print("CHOICES:\n"
                "A. Feel the rooms walls.\n"
                "B. Scream for help.\n"
                "C. Stay still ... Do nothing.\n"
                "D. Go back to sleep.\n")
                
                choice = (input("{} choice: ".format(self.player.name))).upper()

                if choice in ["A", "B", "C", "D"]:

                    if choice == "A":
                        print("{} finds a door.\n"
                        "What should {} do?\n".format(self.player.name, self.player.name))
                        print("CHOICES:\n"
                        "A. Open the door.\n"
                        "B. Try to peak through the keyhole.\n"
                        "C. Scream for help.\n"
                        "D. Knock on the door.\n")

                        choice = (input("{} choice: ".format(self.player.name))).upper()

                        if choice == "A":
                            self.player.state = 'DEAD'
                            print("Congratulations {}, you've \n"
                            "found a portal to hell.\n"
                            "And now you are dead.\n".format(self.player.name))
                            exit()

                        elif choice == "B":
                            self.player.state = 'INSANE'
                            print("Congratulations {}, you've \n"
                            "found a portal to hell.\n"
                            "Realisation of the truth drives \n"
                            "you insane. Not much you can do with \n"
                            "a broken mind.".format(self.player.name))
                            exit()

                        elif choice == "C":
                            self.player.state = 'DEAD'
                            print("The door opens and \n"
                            "{} is attacked by hellhounds.\n"
                            "{} is dead.\n".format(self.player.name, self.player.name))
                            exit()

                        elif choice == "D":
                            self.player.state = 'FRACTURED'
                            print("{} is answered by a \n"
                            "demonic voice. The door swings open\n"
                            "A demon rips {}'s soul from {}'s body.\n"
                            "That is not a good way to go.\n".format(self.player.name, self.player.name, self.player.name))
                            exit()

                        else:
                            print("Not a valid choice... \n"
                            "{}, you see... You are but a pawn \n"
                            "in an elaborate game that you are unable \n"
                            "to fathom\n".format(self.player.name))
                            choice = (input("Your choice: ")).upper()

                    elif choice == "B":
                        print("{}'s voice echoes about the room.\n"
                        "No one answers {}'s call.\n" 
                        "{} hears growling coming from the far end of the room.\n"
                        "What should {} do?\n".format(self.player.name, self.player.name, self.player.name, self.player.name))
                        print("CHOICES:\n"
                        "A. Run in the opposite direction of the growl.\n"
                        "B. Ask who's there.\n"
                        "C. Feel the walls for an exit.\n"
                        "D. Panic !?!!?!!!?!!!!")
                        
                        choice = (input("Your choice: ")).upper()

                        if choice == "A":
                            self.player.state = 'DEAD'
                            print("{} hears the sound of a four legged \n"
                            "creature galloping behind {}, soon enough \n"
                            "it catches up and sinks its teeth into {}.\n"
                            "{} is dead, atleast it was quick...\n".format(self.player.name, self.player.name, self.player.name))
                            exit()

                        elif choice == "B":
                            self.player.state = 'DEAD'
                            print("{} is torn into pieces by a large \n"
                            "four legged creature. Yes {} died.\n".format(self.player.name, self.player.name))
                            exit()

                        elif choice == "C":
                            self.player.state = 'DEAD'
                            print("{}'s hand touches something furry and \n"
                            "wet and now {}'s arm is gone, the \n"
                            "last thing {} sees is red, a very bright red.\n".format(self.player.name, self.player.name, self.player.name))
                            exit()

                        elif choice == "D":
                            self.player.state = 'DEAD'
                            print("While {} panics, {} has an \n"
                            "out of body experience, {} is able to \n"
                            "see {} except {}'s body seems to be \n"
                            "missing {}'s head. Everything fades into \n"
                            "darkness.".format(self.player.name, self.player.name, self.player.name, self.player.name, 
                                                self.player.name, self.player.name))
                            exit()

                        else:
                            print("Not a valid choice... \n"
                            "{}, you see... You are but a pawn \n"
                            "in an elaborate game that you are unable \n"
                            "to fathom\n".format(self.player.name))
                            choice = (input("Your choice: ")).upper()

                    elif choice == "C":
                        print("Time passes, {} grows bored.\n"
                        "What should {} do?\n".format(self.player.name, self.player.name))
                        print("CHOICES:\n"
                        "A. Keep waiting.\n"
                        "B. Take a nap.\n"
                        "C. Feel the walls for an exit.\n"
                        "D. Scream for help.\n")

                        choice = (input("Your choice: ")).upper()

                        if choice == "A":
                            self.player.state = 'LIMBO'
                            print("A door opens at an end of the room \n"
                            "A demon steps in sees {} and speaks \n"
                            "some unintelligible gibberish to {} \n"
                            "The demon casts a spell on {} and \n"
                            "carts {} away to some unknown fate\n"
                            "{} is probably be dead or worse, \n"
                            "by the time it is done with {}.".format(self.player.name, self.player.name, 
                                                                        self.player.name, self.player.name, 
                                                                        self.player.name, self.player.name))
                            exit()

                        elif choice == "B":
                            print("{} wakes up in {}'s bed, \n"
                            "it was all a bad dream, or was it.\n".format(self.player.name, self.player.name))
                            exit()

                        elif choice == "C":
                            self.player.state = 'DEAD'
                            print("As {} feel the walls, \n"
                            "a door suddenly opens a demon steps in \n"
                            "it chops off {}'s head before {} can \n"
                            "do anything.\n"
                            "Thats not very nice of the demon.\n".format(self.player.name, self.player.name, self.player.name))
                            exit()

                        elif choice == "D":
                            self.player.state = 'DEAD'
                            print("As {} screams for help {} is \n"
                            "attacked by a large four legged creature \n"
                            "just before it mauls {} it is killed \n"
                            "by a demon, which then proceeds to rip \n"
                            "out {}'s heart.\n".format(self.player.name, self.player.name, self.player.name, self.player.name))
                            exit()

                        else:
                            print("Not a valid choice... \n"
                            "{}, you see... You are but a pawn \n"
                            "in an elaborate game that you are unable \n"
                            "to fathom\n".format(self.player.name))
                            choice = (input("Your choice: ")).upper()

                    elif choice == "D":
                        print("{} hears a growl in the dark.\n"
                        "What should {} do?\n".format(self.player.name, self.player.name))
                        print("CHOICES:\n"
                        "A. Wake up, do nothing.\n"
                        "B. Keep Sleeping.\n"
                        "C. Scream for help.\n"
                        "D. Wake up, look for an exit.\n")

                        choice = (input("Your choice: ")).upper()

                        if choice == "A":
                            self.player.state = 'DEAD'
                            print("A large four legged creature \n"
                            "attacks {}, it is slain by a demon, \n"
                            "the demon mutters some unintelligible \n"
                            "gibberish after which it snaps {}'s neck.\n".format(self.player.name, self.player.name))
                            exit()
                        
                        elif choice == "B":
                            print("{} wakes in your room feeling refreshed \n"
                            "Not even a bad dream can keep {} down.\n".format(self.player.name, self.player.name))
                            exit()
                        
                        elif choice == "C":
                            self.player.state = 'INSANE'
                            print("As {} screams for help {} spots \n"
                            "a demon performing a ritual next to {} \n"
                            "just before {} is mauled by the \n"
                            "growling creature, {} is instanteneously \n"
                            "transported to {}'s bedroom. Now {} will \n"
                            "live the rest of {}'s life in denial, saying \n"
                            "that didn't happen, but guess what it did. \n"
                            "There are things that go bump at night. \n".format(self.player.name, self.player.name, 
                                                                                self.player.name, self.player.name, 
                                                                                self.player.name, self.player.name, 
                                                                                self.player.name, self.player.name))
                            exit()
                        
                        elif choice == "D":
                            self.player.state = 'DEAD'
                            print("As {} tries to seek out an escape \n"
                            "route {} finds that suddenly {} has been returned \n"
                            "to {}'s room, except {} missing half of {}. \n"
                            "Yes, {} is a goner.".format(self.player.name, self.player.name, 
                                                            self.player.name, self.player.name, 
                                                            self.player.name, self.player.name, 
                                                            self.player.name))
                            exit()
                        
                        else:
                            print("Not a valid choice... \n"
                            "{}, you see... You are but a pawn \n"
                            "in an elaborate game that you are unable \n"
                            "to fathom\n".format(self.player.name))
                            choice = (input("Your choice: ")).upper()
            
        if self.get_location() == "UNIMPLEMENTED":
            print("UNIMPLEMENTED")