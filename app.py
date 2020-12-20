import os
import zipfile

import torch
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class Item(BaseModel):
    passage: str


app = FastAPI()

# transformers
model_name = "model"

if not os.path.isdir(model_name):
    os.mkdir(model_name)
    zipfile.ZipFile("model.zip", "r").extractall(model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# torch
is_cuda = torch.cuda.is_available()
softmax = torch.nn.Softmax(dim=1)

if is_cuda:
    model.cuda()


@app.post("/generate")
async def predict(item: Item):
    data = tokenizer(
        item.passage,
        return_tensors="pt",
    )
    input_ids, token_type_ids, attention_mask = data.values()
    if is_cuda:
        input_ids = input_ids.cuda()
        token_type_ids = token_type_ids.cuda()
        attention_mask = attention_mask.cuda()

    prob = float(softmax(model(input_ids, token_type_ids, attention_mask)[0])[0, 1])

    return {"prob": prob}
