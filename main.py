from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"about page": "Hi. It's me"}
