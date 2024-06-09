import cv2
import os
import string

# Read image
img = cv2.imread("hacker.jpg")

# Take the msg and passcode
msg = input("Enter the message: ")
passcode = input("Enter the passcode: ")

# Create two dictionaries d and c to map the characters to number to create encryption and decryption
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)


n=0 #row
m=0 #col
z=0 #color channel

# Encryption
for i in range(len(msg)):
    img[n,m,z] = d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3

# Write the encrypted msg in img file
# Saving the file
cv2.imwrite("encrypted_img.jpg",img)
# opening the saved file
os.startfile("encrypted_img.jpg")


#decrypted msg
dec_msg = ""
n=0 #row
m=0 #col
z=0 #color channel

#Authenticate the user by password
auth_pass = input("Enter the passcode: ")

if(auth_pass == passcode):
    #decryption
    for i in range(len(msg)):
        dec_msg = dec_msg + c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1)%3
    print("Decrypted msg: ", dec_msg)
else:
    print("Wrong passcode. Unauthorized User")


