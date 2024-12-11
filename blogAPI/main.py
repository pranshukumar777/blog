from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder 
from services.articleService import ArticleService  
from repositorties.articleRepository import ArticleRepository
from models.article import Article  
app = FastAPI() 
articleRepo = ArticleRepository()
articleService = ArticleService(articleRepo)
@app.get("/{id}")
def getHome(id:int):
    return {"message": f"Welcome to my API! ID {id}"}   

@app.get("/articles/{id}")  
def getArticle(id:int):
    resultArticle = articleService.getbyId(id)
    return jsonable_encoder(resultArticle)

@app.post("/articles")
def createArticle(article: Article):
    id = articleService.createArticle(article)
    return {"message":"Created","ArticleId":id}
