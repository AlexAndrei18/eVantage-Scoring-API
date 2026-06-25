import logging #biblioteca care se ocupa cu log urile 
import sys #biblioteca care se ocupa cu afisarea pe ecran

def setup_logger():
    logger = logging.getLogger("AppLogger")

    logger.setLevel(logging.INFO) # ne afiseaza chestii utile de tip INFO si erori grave 

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') # formatul afisat

    console_handler = logging.StreamHandler(sys.stdout) #afisarea pe ecran
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler("app.log") #afisarea in fisier
    file_handler.setFormatter(formatter)

    if not logger.handlers:          #ne asiguram ca nu printam acelasi mesaj de 2 ori 
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

logger = setup_logger()