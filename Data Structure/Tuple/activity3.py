weather = (1,0,0,0,1,1,0)
sunny = 0
rainny = 0
for i in range(0,7):
    if (weather[i]==0):
        rainny = rainny + 1
    else:
        sunny = sunny + 1
if sunny > rainny:
    print("the weather is good")
else:
    print("the weather is bad")