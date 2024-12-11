
from models.article import Article
from repositorties.articleRepository import ArticleRepository


class ArticleService:
    articleRepository:ArticleRepository 
    def __init__(self,articleRepository:ArticleRepository):
        self.articleRepository = articleRepository  
    
    def getbyId(self,articleId)->Article :
        return self.articleRepository.get(articleId)
    
    def createArticle(self,article) ->int:
        return self.articleRepository.createArticle(article)