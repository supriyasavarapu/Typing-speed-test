from time import *
import random as r

print(time())


def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

if __name__ =='__main__':
 while True:
    ck=input(" ready to test : yes / no :")
    if ck == "yes":
        test = ["step1:create a file on desktop.",
        "my name is savrapu supriya","welcome to learning code"]
        test1= r.choice(test)
        print("         ***** typing speed *****")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput=input("Enter : ")
        time_2 = time()

        print('speed : ',speed_time(time_1,time_2,testinput)," w/sec")
        print(" error : ", mistake(test1,testinput))
    elif ck == 'no':
        print( " thank you " )
        break
    else:
        print(" wrong input ")