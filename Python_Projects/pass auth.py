import getpass
database = {"Joy": "11111", "adnan": "56789"}

username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
  if username == i:
    while password != database.get(i):
        password = getpass.getpass("Enter Your Password Again : ")
    break
  else :
      print("You are not an user !")
      break

    




