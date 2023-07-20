#empezar

email = input("Ingresa tu email :")

user = email[:email.index("@")]

dominio = email[email.index("@")+1:]

print(f"Tu usuario es {user}")
print(f"El dominio de tu email es {dominio}")