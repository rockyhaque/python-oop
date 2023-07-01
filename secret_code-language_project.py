# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode




""" 

# ! Working project
import random

def code(message):
  if len(message) >= 3:
    first_letter = message[0]
    message = message[1:] + first_letter
    secret_message = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(3)]) + message + ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(3)])
  else:
    secret_message = message[::-1]
  return secret_message

def decode(secret_message):
  if len(secret_message) <= 3:
    secret_message = secret_message[::-1]
    last_letter = secret_message[-1]
    secret_message = secret_message[:-1] + last_letter
  else:
    secret_message = secret_message[3:-3]
    last_letter = secret_message[-1]
    secret_message = secret_message[:-1] + last_letter
  return secret_message


def main():
  choice = input("Do you want to code (c) or decode (d)? ")
  message = input("Enter your message: ")

  if choice == "c":
    secret_message = code(message)
    print("Your secret message is:", secret_message)
  elif choice == "d":
    secret_message = decode(message)
    print("Your decoded message is:", secret_message)
  else:
    print("Invalid choice.")

if __name__ == "__main__":
  main()


"""


# Another approach
st = input("Enter message: ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding: ")
coding = True if (coding=="1") else False
print(coding)
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      r1 = "dsf"
      r2 = "jkr"
      stnew = r1+ word[1:] + word[0] + r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
