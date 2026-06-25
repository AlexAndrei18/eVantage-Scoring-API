import os #import operating system 
class Config: 
    APP_NAME = os.getenv("APP_NAME", "eVantage Scoring API") #cautam setarea APP_NAME,iar daca nu o gasim folosim un nume de rezerva
    DEBUG_MODE = os.getenv("DEBUG_MODE", "True") #il setam pe true ca sa putem vedea erorile 
settings = Config() #salvam setarile in variabila settings ca sa le putem folosi in main.py