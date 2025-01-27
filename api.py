import os
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import asyncio

os.environ["TOKENIZERS_PARALLELISM"] = "false"

app = FastAPI()

guard_tokenizer = AutoTokenizer.from_pretrained("ProtectAI/deberta-v3-base-prompt-injection-v2")
guard_model = AutoModelForSequenceClassification.from_pretrained("ProtectAI/deberta-v3-base-prompt-injection-v2")

classifier = pipeline(
  "text-classification",
  model=guard_model,
  tokenizer=guard_tokenizer,
  truncation=True,
  max_length=512,
  device=torch.device("cuda" if torch.cuda.is_available() else "cpu"),
)

class PredictionRequest(BaseModel):
    texts: List[str]

class PredictionResponse(BaseModel):
    predictions: List[dict]

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    try:
        predictions = await asyncio.to_thread(classifier, request.texts)
        return PredictionResponse(predictions=predictions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)
