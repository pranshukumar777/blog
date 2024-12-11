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
        return Article(*row)
