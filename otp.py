# Import the pyotp library for OTP generation
import pyotp

# Generate a new Time-based One-Time Password (TOTP) object with a random secret key
totp = pyotp.TOTP(pyotp.random_base32())

# Print the secret key used for generating OTPs
print('OTP Secret:', totp.secret)

# Generate the current OTP based on the secret key
otp_code = totp.now()

# Print the current OTP
print('OTP Code:', otp_code)

# Get user input for the OTP verification
user_input = input("Enter the OTP: ")

# Verify the user input against the current OTP
result = totp.verify(user_input)

# Check the result of the OTP verification
if result:
    print("OTP Code is valid!")
else:
    print("OTP is Invalid")