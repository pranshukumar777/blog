from sqlalchemy import text 
from .baseRepository import BaseRepo 
from models.article import Article 
class ArticleRepository(BaseRepo):
    def __init__(self):
        super().__init__() 
    
    def get(self,id):
        with self.engine.connect() as conn: 
            query = f"select Id ,Title,Content from article where Id = {id}" 
            result =  conn.execute(text(query))  
            row = result.fetchone() 
        return Article.model_construct(row)
    
    def createArticle(self,article:Article):
        with self.engine.connect() as conn: 
            query = f"INSERT INTO article (Title, Content) VALUES ('{article.title}', '{article.content}')"
            conn.execute(text(query))
            id = conn.execute(text("SELECT last_insert_id()")).fetchone()[0]
            conn.commit()
        return id  
