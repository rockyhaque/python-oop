#Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.

import random

questions = [
  ["Which programming language is used to build blockchain applications?", "Solidity", "Python", "Java", "C++", 1],
  ["Which programming language is used to build web3 applications?", "JavaScript", "Python", "Solidity", "Rust", 2],
  ["Which programming language is used to build DeFi applications?", "Solidity", "JavaScript", "Python", "Go", 3],
  ["Which programming language is used to build NFT applications?", "Solidity", "JavaScript", "Python", "C++", 4],
  ["Which programming language is used to build data science and machine learning models?", "Python", "R", "Java", "C++", 2],
  ["Which programming language is used to build natural language processing applications?", "Python", "Java", "C++", "R", 1],
  ["Which programming language is used to build computer vision applications?", "Python", "Java", "C++", "JavaScript", 1],
  ["Which programming language is used to build robotics applications?", "Python", "Java", "C++", "JavaScript", 1],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(0, len(questions)):
  question = questions[i][0]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(question)
  print(f"a. {questions[i][1].ljust(15)}       b. {questions[i][2].ljust(15)}")
  print(f"c. {questions[i][3].ljust(15)}       d. {questions[i][4].ljust(15)}")

  reply = input("Enter Your Answer (a/b/c/d or  0 to quit):\n" )
  if (reply == "a"):
    reply = 1
  elif (reply == "b"):
    reply = 2
  elif (reply == "c"):
    reply = 3
  elif (reply == "d"):
    reply = 4
  elif (reply == "0"):
    break

  if (reply == questions[i][-1]):
    print(f"Correct answer! You have won Rs. {levels[i]}")
    money += levels[i]
  else:
    print("Wrong answer!")
    break

print(f"Your Take Home money is {money}")
