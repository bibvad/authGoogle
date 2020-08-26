import pyotp
totp = pyotp.TOTP("BZD7OZUSARYKVDUZ")
notp = totp.now()
print(totp.now())
passw = input("Code:")

print(totp.verify(passw))