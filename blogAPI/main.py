from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder 
from repositorties.articleRepository import ArticleRepository
# from models.article import Article  
app = FastAPI() 
articleRepository = ArticleRepository()
@app.get("/{id}")
def getHome(id:int):
    return {"message": f"Welcome to my API! ID {id}"}   

@app.get("/articles/{id}")  
def getArticle(id:int):
    resultArticle = articleRepository.get(id)
    return jsonable_encoder(resultArticle)