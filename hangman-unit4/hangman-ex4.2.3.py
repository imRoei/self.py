temperature = input("Insert the temperature you would like to convert: ")
if(temperature[-1]=='C'):
    print(int(float(temperature[:-1])+int(32*5))/5)
elif(temperature[-1]=='F'):
    F = (int(temperature[:-1])*5-160)/9
    print(F)