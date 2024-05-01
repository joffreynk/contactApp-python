import pyinputplus as pip, re, sys, pprint

contacts = {}

contact = {'name':{'tel':75652, 'email':'joy@example.com'}}

def enterName():
  return pip.inputStr('Enter the contact name: ', allowRegexes=r'^([A-Za-z0-9_*=-%]*\s[A-Za-z0-9_*=-%]*)+$', )

def enterPhoneNumber():
  return pip.inputStr('Enter the phone number: ', allowRegexes=r'^(76|79|72|78|69|68|62|61)\d{6})$' )

def enterEmail():
  return pip.inputStr('Enter the email address: ', allowRegexes=r'^[a-zA-Z0-9.%+_-]+@[a-zA-Z0-9.%+_-]+\.[a-z]+$')



def displayContacts(allcontacts):
  count = 1
  for k, v in allcontacts.items():
    print('{}. {}: {}'.format(count, k, v['telephone']))
    count += 1
  

def createContact():
  contacts[enterName()] = {'telephone': enterPhoneNumber(), 'email': enterEmail()}

def findContact():
  proposedContacts = {}
  name = enterName()
  for contactName in contacts.keys():
    if contactName.startswith(name) or contactName.endswith(name):
      proposedContacts[contactName] = contacts[contactName]
  if len(proposedContacts):
    print('\nList Contacts found')
    displayContacts(proposedContacts)
    if len(proposedContacts) > 1:
      option = pip.inputYesNo("would you like to choose a specific contact?")
      if option == 'yes':
        choice = pip.inputInt('Enter the contact number, for example: 1')
      
    
  else:
    print("No contact found with name: " + name)
  
def editContact():
  print('edit contact')

def deleteContact():
  print('delete contact')

def printOptions():
  print('''
1. Create a new contact
2. Display all contacts
3. Edit an existing contact
4. Find a contact
5. Delete a contact
6. Exit the program
''')

while True:
  printOptions()
  option = pip.inputInt('Enter your option: ', min=1, max=6)
  match option:
    case 1: createContact()
    case 2: 
      print('\nList of all contacts')
      displayContacts(contacts)
      break
    case 3: editContact()
    case 4: findContact()
    case 5: deleteContact()
    case 6: sys.exit()
    case _: print('Please enter a valid option: ')