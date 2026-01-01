from fastapi import FastAPI
import random

app = FastAPI()

shayari = {
    "love": [
        "Tumhari muskurahat meri duniya hai",
        "Ishq woh hai jo lafzon ka mohtaaj nahi",
        "Tum saath ho toh har dard kam lagta hai"
    ],
    "sad": [
        "Khamoshi bhi kabhi kabhi cheekh jaati hai",
        "Dil toota hai par awaaz nahi aayi",
        "Akele rehna hi behtar lagta hai"
    ],
    "friendship": [
        "Dosti sirf saath rehne ka naam nahi",
        "Saccha dost wahi jo bura waqt dekhe",
        "Dosti mein shartein nahi hoti"
    ],
    "motivation": [
        "Girkar uthna hi asli jeet hai",
        "Mehnat chupchaap karo",
        "Khud par bharosa rakho"
    ]
}

@app.get("/shayari/{category}")
def get_shayari(category: str):
    category = category.lower()
    if category not in shayari:
        return {"error": "Invalid category"}
    return {
        "shayari": random.choice(shayari[category])
    }
