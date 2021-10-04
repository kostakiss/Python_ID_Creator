import random as ran
import webbrowser
import secrets
import string
from time import sleep
def MakePasswd(LEN):
    alphabet = string.ascii_letters + string.digits
    passwd = ''.join(secrets.choice(alphabet) for i in range(LEN))
    return(passwd) #return complete passwd


def Main():
    img = 'https://thispersondoesnotexist.com/'
    email = 'https://10minutemail.com/'

    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe")) #change to chrome.exe directory

    choice = int(input("enter 1 for basic info or 2 for complete id and output to 'output.txt'... "))
    f_num = ran.randint(0, 999)
    s_num = ran.randint(0, 998)
    age = ran.randint(18, 70)

    b_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    type = (ran.choice(b_types))

    last = open('last_names.txt', 'r') #change to last_names.txt path
    lines=last.readlines()
    lastn = (lines[f_num])
    last.close()

    first = open('first_names.txt', 'r') #change to first_names.txt path
    lines=first.readlines()
    firstn = lines[s_num]
    first.close()

    password = MakePasswd(12) #change to desired length
    txt = (f'\n{lastn}{firstn}age: {age}, type: {type}, passwd: {password} (optional)Platform:    (optional)Account name:\nemail url: {email} image url: {img}\n')

    if choice == 1:
        print(f"Credentials:\n{lastn}{firstn}\nAge:{age}")
        sleep(4)   #69 nice
    elif choice == 2:
        print(f'Credentials:\n{lastn}{firstn}\nAge:{age}\nblood type: {type}\nyour account password is {password}\ncreating pfp and disposable email...')
        sleep(1)
        webbrowser.get('chrome').open_new(img) 
        webbrowser.get('chrome').open_new(email)
        wr = open('output.txt', "a") #adds content to output #change to output.txt path
        wr.write(f'{txt}')
        wr.close
        sleep(2)
    else:
        print("invalid choice")
        sleep(1)
        pass
if __name__ == '__main__':
    Main() #call the function