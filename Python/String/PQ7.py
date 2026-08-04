"clean phone number"
#take a phone no. as input
#in the format +91-xxxxx-xxxxx
#remove all dashes and the country code
#print the clear 10 digit number

def phone_check(phone:str):
    phone = phone.replace("+91-","")
    phone = phone.replace("-","")
    print("Clean phone number", phone)

phone = input("Enter Phone Number in format +91- add as a country code +91-xxxxx-xxxxx: ")
phone_check(phone)