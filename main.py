import os
from fastapi import FastAPI, Body, HTTPException, Query
import database_handler
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

api_key = os.environ.get("GEMINI_API_KEY", "AIzaSyBs0siC0rUOwSUkLwNlV1L6PqsNzu9oBJ4")
client = genai.Client(api_key=api_key)

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/recipes")
def get_all_recipes(category: str = None):
    return database_handler.read_recipes(category)

@app.get("/recipes/{recipe_id}")
def get_recipe_by_id(recipe_id: int):
    recipe = database_handler.get_recipe_by_id(recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="המתכון לא נמצא")
    return recipe

@app.post("/recipes")
def add_recipe(name: str = Body(...), instructions: str = Body(...), category_id: int = Body(1), user_id: int = Body(1)):
    success = database_handler.add_recipe(name, instructions, category_id, user_id)
    if success:
        return {"message": "המתכון נוסף בהצלחה ל-SQL!"}
    raise HTTPException(status_code=500, detail="שגיאה בהוספה ל-SQL")

@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, name: str = Body(None), instructions: str = Body(None)):
    success = database_handler.update_recipe(recipe_id, name, instructions)
    if not success:
        raise HTTPException(status_code=404, detail="המתכון לעדכון לא נמצא")
    return {"message": f"מתכון {recipe_id} עודכן בהצלחה"}

@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    success = database_handler.delete_recipe(recipe_id)
    if not success:
        raise HTTPException(status_code=404, detail="המתכון למחיקה לא נמצא ב-SQL")
    return {"message": f"מתכון מספר {recipe_id} נמחק בהצלחה"}


@app.get("/ask")
def ask(question: str = Query(...)):
    try:
        api_key = os.environ.get("GEMINI_API_KEY", "AIzaSyBs0siC0rUOwSUkLwNlV1L6PqsNzu9oBJ4")
        global client
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question,
            config=genai.types.GenerateContentConfig(
                system_instruction="אתה שף מקצועי. ענה אך ורק על אוכל ומתכונים."
            )
        )
        return {"answer": response.text}
    except Exception as e:
        print(f"Gemini Error: {e}")
        return {"answer": "השף הפרטי עסוק כרגע במטבח (בעיית חיבור לרשת), אנא נסו לשאול שוב מאוחר יותר!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)