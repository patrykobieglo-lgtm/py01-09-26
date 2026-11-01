email = " Jan.Kowalski@Gmail.COM "
email = email.strip()
email = email.lower()
print(email)
print("@" in email) #czy @ znajduje się w email
login, domena = email.split("@")
print(login)
print(domena)


