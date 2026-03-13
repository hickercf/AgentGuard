import os
import json


class VectorDB:

    def __init__(self):

        self.data = []


    def load(self, path="app/knowledge_base"):

        for file in os.listdir(path):

            if file.endswith(".json"):

                full = os.path.join(path, file)

                with open(full, "r", encoding="utf-8") as f:

                    content = json.load(f)

                    self.data.append(content)


    def search(self, query):

        results = []

        for doc in self.data:

            text = json.dumps(doc, ensure_ascii=False)

            if query.lower() in text.lower():

                results.append(doc)

        return results[:3]