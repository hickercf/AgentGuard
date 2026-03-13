from app.vector_store.vector_db import VectorDB


class RAGService:

    def __init__(self):

        self.db = VectorDB()

        self.db.load()


    def query(self, text):

        return self.db.search(text)