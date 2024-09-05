from dotenv import load_dotenv
from models.Hero import Hero
from models.Super import Super
from models.Administrator import Administrator

if __name__ == "__main__":
    load_dotenv()

#    Administrator.insert()


    for key in Administrator.get_all():
        print(key)
        
    print(Administrator.sign_in(input("Login: "), input("Senha: ")))
