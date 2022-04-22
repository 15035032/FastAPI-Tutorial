from fastapi import FastAPI

app = FastAPI()



@app.get('/item/{item_id}')
async def root(item_id):
    return {"item_id":"item_id"}

    