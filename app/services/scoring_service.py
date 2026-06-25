from app.models import LoanInput, RiskOutput

def calculate_risk(data : LoanInput) -> RiskOutput:
    #normalizam si folosim min(... , 1.0) ca plasa de siguranta sa nu depasim limita maxima.
    norm_income = min(data.income / 100000, 1.0)
    norm_loan = min(data.loan_amount / 50000, 1.0)
    norm_credit = data.credit_score / 850

    #norm_loan - direct proportional ,norm_income - invers proportional ,norm_credit - invers proportional 
    risk_score = (norm_loan * 0.4) +((1-norm_income) * 0.3) + ((1-norm_credit) * 0.3)
    risk_score = max(0.0, min(risk_score, 1.0))

    if risk_score <=0.3 :
       category = "LOW"
    elif risk_score <= 0.7 :
        category = "MEDIUM"
    else:
        category= "HIGH"

    return RiskOutput(
       risk_score = round(risk_score,2),
       risk_category = category

    )