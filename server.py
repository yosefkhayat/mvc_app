from fastapi import FastAPI


server = FastAPI()

#test the server is up
@server.get("/")
def sanity_check():
    return {"msg" : "The server is working properly!"}