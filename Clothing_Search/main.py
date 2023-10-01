import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserRequestIn(BaseModel):
    new_sentence: str
    n: int

class PredictionOut(BaseModel):
    pred: List[Dict[str, str]]

model = SentenceTransformer('all-mpnet-base-v2')

data = pd.read_excel("cloths.xlsx")

d = data['Product URL'].tolist()
Target = data['Product Name'].tolist()
existing_sentences = data['Product Name'].astype(str).tolist()
sentence_embeddings = model.encode(existing_sentences)

@app.post("/Clothing_Search", response_model=PredictionOut)
def extract_entities(user_request: UserRequestIn):
    new_sentence = "I want to do " + user_request.new_sentence.lower()
    n = user_request.n

    new_embeddings = model.encode([new_sentence])[0]
    similarity = cosine_similarity(
        [new_embeddings],
        sentence_embeddings
    )

    pred = similarity[0].tolist()
    combined = sorted(zip(pred, d, Target), reverse=True)
    n_pred, top_n_id, top_n_data = zip(*combined)

    # Limit the number of results to 'n'
    n = min(n, len(existing_sentences))
    pred_lst = []

    for i in range(n):
      if n_pred[i] < 0.15:
        break
      res = {
            'similarity': n_pred[i],
            'URL': top_n_id[i],
            'Name of the product': top_n_data[i]
        }
      pred_lst.append(res)

    return {"pred": pred_lst}
