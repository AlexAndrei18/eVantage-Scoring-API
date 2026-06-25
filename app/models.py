from pydantic import BaseModel

class LoanInput(BaseModel) :
    age : int
    income : float
    loan_amount : float
    credit_score : int 

class RiskOutput(BaseModel) :
    risk_score : float
    risk_category : str