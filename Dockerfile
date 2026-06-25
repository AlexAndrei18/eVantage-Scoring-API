# folosim o versiune de python cat mai mica (slim) ca sa nu ocupe mult spatiu pe server
FROM python:3.10-slim
# setam locul unde o sa stea aplicatia noastra in interiorul containerului
WORKDIR /app_data
# copiem fisierul cu librariile necesare ca sa le instalam separat
COPY requirements.txt .
# instalam librariile. --no-cache-dir e ca sa nu pastram fisiere temporare inutile
RUN pip install --no-cache-dir -r requirements.txt
# copiem tot codul nostru din folderul app de pe laptop in folderul app din container
COPY ./app ./app
# deschidem portul 8000 ca sa putem comunica cu aplicatia din exterior
EXPOSE 8000
# comanda care porneste serverul automat cand containerul este pornit
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
