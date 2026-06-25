from fastapi import FastAPI,HTTPException 
from app.models import LoanInput, RiskOutput
from app.services.scoring_service import calculate_risk
from app.utils.logger import logger 
from app.config import settings

# pornim aplicatia si ii punem titlul citit din fisierul nostru de config
app = FastAPI(title = settings.APP_NAME)

# cream adresa web /predict prin care aplicatia primeste date (metoda POST)
# de asemenea, ii spunem sa valideze raspunsul final pe baza sablonului RiskOutput
@app.post("/predict", response_model = RiskOutput)
def predict_loan_risk(payload : LoanInput) :
    # notam in fisierul de loguri ca am primit o cerere, ca sa avem un istoric
    logger.info(f"Cerere noua primita: Varsta={payload.age}, Venit={payload.income}")
    try:
        # dam datele algoritmului nostru 
       result=calculate_risk(payload)
       # daca totul a mers bine, notam succesul si returnam rezultatul clientului
       logger.info(f"Evaluare finalizata cu succes. Categoria: {result.risk_category}")
       return result
    except Exception as eroare:
        # plasa de siguranta: daca ceva crapa, salvam eroarea reala in loguri ca sa o investigam noi
        logger.error(f"Eroare interna la calcularea riscului: {str(eroare)}")
        # totodata ii afisam clientului un mesaj si codul de eroare 
        raise HTTPException(status_code=500, detail="Ne cerem scuze,a aparut o eroare interna la calcul")