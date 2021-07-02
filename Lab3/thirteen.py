'''
  Building the car game ::
  CAR GAME:
        > help
          start - to start the car
          stop - to stop the car
          quit - to exit
        > asd
          I don't understand this
        > start
          Car started... Ready to go!!
          >start
           Car had already started!!
        > stop
          Car stopped..
          >stop
           Car had already stopped!!
        > quit
'''
stop = True
started = False                                                   #carhasnotstartedyet.
value = ""                                                        #identifier
while True :
    value = str(input("Enter the command for the game:")).lower()
    if value == 'start' :
        if started == False:
            print(" car  started. Ready to go...")
        else :
            started = True                                          #carhasstartedthiswillwork
            print("The car has already started.")
    elif value == "stop":
            if stop == True :
                print("Car stopped")
            else :
                stop = False
                print ("Car has already stopped.")
    elif value == 'help' :
            print ('start - to start the car')
            print ('stop - to stop the car')
            print ('quit - to exit')
    elif value == 'quit':
            print ("quit")
            break
    else :
        print("I don't understand this.")



