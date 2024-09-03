from dotenv import load_dotenv
from models.Super import Super

if __name__ == "__main__":
    load_dotenv()
    
    goku = Super.insert()
    
    print(goku)
