# eVantage Fintech Scoring API

Acesta este un API pentru evaluarea riscului de credit (Loan Risk Scoring), construit cu FastAPI și Python. Aplicația primește datele financiare ale unui client și returnează un Scor de Risc și o Categorie (LOW, MEDIUM, HIGH).

## Structura Proiectului
Proiectul respectă o structură modulară:
* `models.py` - Validarea datelor de intrare/ieșire folosind Pydantic.
* `scoring_service.py` - Logica de business (calculul matematic).
* `logger.py` - Salvarea activității pe consolă și în `app.log`.
* `config.py` - Citirea setărilor din Variabilele de Mediu.
* `main.py` - Rutele API-ului și gestionarea erorilor.

## Cum să rulezi aplicația local
1. Instalează pachetele necesare: `pip install -r requirements.txt`
2. Pornește serverul: `uvicorn app.main:app --reload`
3. Accesează documentația: `http://127.0.0.1:8000/docs`

## Cum să rulezi aplicația cu Docker
1. Construiește imaginea: `docker build -t evantage-scoring-api .`
2. Pornește containerul: `docker run -p 8000:8000 evantage-scoring-api`