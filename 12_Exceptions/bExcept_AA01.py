import validate_email
#email = input("Geben Sie Ihre e-Mail Adresse ein:")

email = "abc@def.fr"


try:
    email = validate_email
    print(str(email))
except:
    print("Error DU elender Gumpfi")
