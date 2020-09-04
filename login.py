import pyotp
totp = pyotp.TOTP("BZD7OZUSARYKVDUZ")
passw=''

while passw != 'Exit':
    passw = input("Code:")
    print(totp.verify(passw))
