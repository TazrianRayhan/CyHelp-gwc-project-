
cybersecurityBirthYear = 1970

#Greets user
print("Hello there! I'm CyHelp. I can explain topics about cybersecurity.")
userName = input("What's your name? \n")

print("Hi there, "+ userName +"!" )
todaysYear = input("What year it is right now? \n")

timePassed = int(todaysYear) - cybersecurityBirthYear

print("Wow! "+ userName + ", did you know that it's been "+ str(timePassed) + " years since Cybersecurity began?")

#Recounts start of Cybersecurity
print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!\n")

#Describes Cybersecurity
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from cyber attacks.")

print("These people can be governments/nations, individuals, companies,  community organizations, and hackers.\n")

input("press ENTER to continue. \n")
#Introduces CIA Triad
print("The CIA Triad is the model used to discuss cybersecurity. The CIA Triad is a widely accepted model within the cybersecurity industry that outlines the three core objectives of any cybersecurity program.\n The triad consists of three components: Confidentiality, Integrity, and Availability.")
print("Would you like to learn more about the CIA triad?")

giveInfo = input("Type 'yes' or 'no'\n")


#Explains pillars of CIA Triad
while giveInfo.lower() == 'yes':
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n (a) Confidentiality \n (b) Integrity \n (c) Availability \n (d) None")
  
  topic = input()
  
  if topic.lower() == "a":
    print("Confidentiality makes sure that data is private.")
  elif topic == "b":
    print("Integrity makes sure data has not been tampered with and can be trusted.")
  elif topic == "c":
   print("Availability makes sure authorized people can access the data.")
  elif topic == "d":
   break
  else:
    print("Sorry, I didn't catch that. Please choose from the options above.")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")