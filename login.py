import pyotp
totp = pyotp.TOTP("BZD7OZUSARYKVDUZ")

while passw != 'Exit':
    passw = input("Code:")
    print(totp.verify(passw))
