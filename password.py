from playsound import playsound
import os
import time
wc=0 
print(os.path.dirname(__file__))
while 1:
    print('\nEnter Password : ',end='')
    s=input()
    if s!='password':
        wc+=1
        print('\t\tWrong Password. You may not enter.',wc)
        playsound(os.path.dirname(__file__)+'\error.mp3')
        if wc==5:
            print('\n\n\tToo many wrong attempts...Try after 30 seconds\n')
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