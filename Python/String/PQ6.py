"Email Validation"
#take an email as input 
#validate that it contain exactly 1 @
#and atleast one .
#print valid or invalid


def check_mail(mail:str):
    if "." in mail and mail.count("@") == 1 :
        print("valid")
    else:
        print("Not valid") 

mail = input("Enter ur mail id: ")
check_mail(mail)
