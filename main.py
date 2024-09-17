from dotenv import load_dotenv
from system.System import System

if __name__ == "__main__":
    load_dotenv()
    system = System()
    system.run()