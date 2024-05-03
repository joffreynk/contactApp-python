import pyinputplus as pip, re, sys, pprint

contacts = {}

contact = {'name':{'tel':75652, 'email':'joy@example.com'}}

def enterName(empt=False):
  return pip.inputStr('Enter the contact name: ', allowRegexes=r'^([A-Za-z0-9_*=-%]*\s[A-Za-z0-9_*=-%]*)+$', blank=empt).strip().title()

def enterPhoneNumber(empt=False):
  return pip.inputStr('Enter the phone number: ', allowRegexes=r'^(76|79|72|78|69|68|62|61)\d{6})$', blank=empt ).strip()

def enterEmail(empt=False):
  return pip.inputStr('Enter the email address: ', allowRegexes=r'^[a-zA-Z0-9.%+_-]+@[a-zA-Z0-9.%+_-]+\.[a-z]+$', blank=empt).strip()


def displayContacts(allcontacts):
  count = 1
  for k, v in allcontacts.items():
    print('{}. {}: {}'.format(count, k, v['telephone']))
    count += 1
  print('\n')
  

def createContact():
  contacts[enterName()] = {'telephone': enterPhoneNumber(), 'email': enterEmail()}

def finder(contacts, key):
  proposedContacts = {}
  for contactName in contacts.keys():
    if contactName.startswith(key) or contactName.endswith(key):
      proposedContacts[contactName] = contacts[contactName]
  return proposedContacts

def NoContactsmessage():
  print("You don't have any contacts, please add them to the list")

def findContact(contacts):
  if (len(contacts))<1:
    NoContactsmessage()
    return None
  name = enterName()
  proposedContacts = finder(contacts, name)
  if len(proposedContacts):
    print('\nList Contacts found')
    displayContacts(proposedContacts)
    if len(proposedContacts) > 1:
      option = pip.inputYesNo("would you like to choose a specific contact?")
      if option == 'yes':
        choice = pip.inputInt('Enter the contact number, for example, 1: ', min=1, max=len(proposedContacts))
        keys = list(proposedContacts.keys())
        return {keys[choice-1]: proposedContacts[keys[choice-1]]}
      return None
    return proposedContacts
  else:
    print("No contact found with name: " + name)
  
def editContact():
  contact = findContact(contacts)
  if contact is None:
    NoContactsmessage()
  else:
    name = enterName(True)
    tel = enterPhoneNumber(True)
    email = enterEmail(True)
    keys =  list(contact.keys())
    if len(tel):
      contacts[keys[0]]['telephone'] = tel
    if len(email):
      contacts[keys[0]]['email'] = email
    if len(name):
      contacts[name] = contacts[keys[0]]
      del contacts[keys[0]]
      
def deleteContact():
  contact = findContact(contacts)
  if contact is None:
    NoContactsmessage()
  else:
    keys = list(contact.keys())
    del contacts[keys[0]]

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
    case 3: editContact()
    case 4: findContact(contacts)
    case 5: deleteContact()
    case 6: sys.exit()
    case _: print('Please enter a valid option: ')