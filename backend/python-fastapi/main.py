# FastAPI Main
from fastapi import FastAPI
import openai

app = FastAPI()

@app.get("/ai-decision")
async def ai_decision():
    # TODO: Call OpenAI API and return decision
    return {"decision": "mock decision"}