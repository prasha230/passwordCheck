print("Welcome to password checker! \n")
from playsound import playsound
import os
import time
print(os.path.dirname(__file__))
wc=0
while 1:
    print('\nEnter Password : ',end='')
    s=input()
    if s!='password':
        wc+=1
        print('\t\tWrong Password. You may not enter.')
        playsound(os.path.dirname(__file__)+'\error.mp3')
        if wc==5:
            print('\n\n\tToo many wrong attempts...Try again after 10 seconds\n')
            t=10
            while t!=-1:
                print('Retry in {:02d} seconds...'.format(t),end='\r')
                time.sleep(1)
                if t==0:
                    print('\rTry now               ')
                t-=1
            wc=0
    else:
        print('\n\t\tWelcome. You may enter.\n')
        playsound(os.path.dirname(__file__)+'\correct.mp3')
        exit()

# This is a password checker application.
# correct password is "password."
# Maximum 5 attempts allowed
# Sound alerts for correct and incorrect password