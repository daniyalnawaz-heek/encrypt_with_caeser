def encrypt(text,Shift):
  result = ""
  
   # transverse the plain text
  for i in range(len(text)):
      char = text[i]
      cp = chr(ord(char)+Shift)
      result += cp 
  return result



text = str(input("Enter the text"))
Shift = int(input("enter the shifting no"))
cipher=encrypt(text,Shift)
print("Cipher text is: " + cipher +"  " + "shift key is" + str(Shift))




