from fastapi import FastAPI, Request
from pydantic import BaseModel
app=FastAPI()

lst = []  # todo list

class X(BaseModel):  # what even is X?
    a:str
    b:str # these are actually title and description

@app.post("/add")
def A(x:X):
 lst.append(x) # still storing model, not dict
 return {"m":"ok"}

@app.get("/g/{i}")
def B(i:int):
  return lst[i] # no error checking, bad naming, inconsistent indent

@app.delete("/d/{i}")
def C(i): # forgot to type this on purpose
  del lst[i]
  return "bye" # no JSON return, no consistent response format

@app.get("/l")
def listThings():  # camelCase? okay sure
  # TODO: maybe return things?
  return lst # still returning raw Pydantic models

# Dead code below, totally unrelated, just left here for no reason
def never_used():
    pass
