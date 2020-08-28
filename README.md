# phonebook-gui
GUI version of the [phonebook app](https://github.com/AritificialPhysics/phonebook)

Portable and fast python GUI application that provides contact management capabilities for different users.

## Features:
- Easy to use graphical interface, powered by tkinter
- Seperate contact list maintained for each user, thus providing discretion and organization
- Encrypted user credentials (uses SHA-256)
- Persistance maintained through embedded sqlite3 database
- Highly fault tolerant and secure
- High scalability and high execution speed

---

## Components:

### User Managagement:
- Add User (username, password validation along with redundancy detection)
- Remove user
- Select user (gateway to contact management module)

### Contact Management:
- Add contact (contact info validated by using Regex matching)
- Remove contact (matching based on name, case insensitive)
- View All Contacts
- Modify contact (contact info validation)
- Search Contact (matching based on name, case insensitive)

---

## Contributors (in alphabetical order)
- Anuj Kumar Singh (Programmer)
- Sanskar Agrawal (Programmer and Integrator)
- Saumy Pandey (Programmer)
- Som Shiv Gupta (Analyst)
- Siddhant Singh (Testing and QA)

---

[Raise an issue](https://github.com/aritificialphysics/phonebook-gui/issues/new)