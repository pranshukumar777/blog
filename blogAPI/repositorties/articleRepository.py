from sqlalchemy import text 
from .baseRepository import BaseRepo 
from models.article import Article 
class ArticleRepository(BaseRepo):
    def __init__(self):
        super().__init__() 
    
    def get(self,id):
        with self.engine.connect() as conn: 
            query = f"select id ,title,content from article where Id = {id}" 
            result =  conn.execute(text(query))  
            row = result.fetchone() 
        return Article.model_construct({'id','title','content'},**row._mapping)
    
    def createArticle(self,article:Article):
        with self.engine.connect() as conn: 
            query = f"INSERT INTO article (title, content) VALUES ('{article.title}', '{article.content}')"
            conn.execute(text(query))
            id = conn.execute(text("SELECT last_insert_id()")).fetchone()[0]
            conn.commit()
        return id  
