''' You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of
the 10 stops on the way. How long will the bus journey take? Alternatively, you could run to
university. You jog the first mile at 7mph; then run the next two at15mph;
before jogging the last at 7mph again. Will this be quicker or slower than the bus?
'''

#bus
DistanceInMiles = 4
SpeedInmph = 25
StoppedTime = 2
NumberOfStop = 10
StopTime = (StoppedTime*NumberOfStop)
Time_1 = (StopTime)/60
Time = (DistanceInMiles//SpeedInmph)
TotalTimeForBus = float(Time_1 + Time)
print(f'The total time taken by bus is {TotalTimeForBus}:')

#jog
FirstDistanceInMiles = 1
FirstSpeed = 7
FirstTime = (1/7)
SecondDistanceInMiles = 2
SecondSpeed = 15
SecondTime = (2/15)
ThirdDistanceInMiles = 1
ThirdSpeed = 7
ThirdTime = (1/7)
TotalTimeForJogging = float(FirstTime+SecondTime+ThirdTime)
print(f'The total time taken by jogging is {TotalTimeForJogging}:')

if TotalTimeForBus<TotalTimeForJogging :
    print(f'Jogging is quicker than bus:')
else :
    print(f'Bus is quicker than jogging:')