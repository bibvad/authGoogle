import pyotp
import qrcode

import pyotp

base32secret = pyotp.random_base32()
print('Secret:', base32secret)

totp_uri = pyotp.totp.TOTP(base32secret).provisioning_uri(
    "bibvad@gmail.com",
    issuer_name="Secure App")
print(totp_uri)

filename = "site.png"
img = qrcode.make(totp_uri)
img.save(filename)
img.show()


