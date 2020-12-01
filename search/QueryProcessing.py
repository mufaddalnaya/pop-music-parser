import math
from . import doc  

class QueryProcessing:

    def __init__(self, lyrics):
        self.docs = []
        for doc in lyrics:
            self.docs.append(doc)
            
        self.title_words = set()
        for lyrics in self.docs:
            for word in lyrics['title']:
                self.title_words.add(word)

        
        self.body_words = set()
        for lyrics in self.docs:
            for word in lyrics['body']:
                self.body_words.add(word)

        self.title_words_list = []
        for word in self.title_words:
            self.title_words_list.append(word)

        self.body_words_list = []
        for word in self.body_words:
            self.body_words_list.append(word)

        self.title_indexes = {}
        for idx, word in enumerate(self.title_words_list):
            self.title_indexes[word] = idx

        self.body_indexes = {}
        for idx, word in enumerate(self.body_words_list):
            self.body_indexes[word] = idx

        self.docVectors = []
        for doc in self.docs:
            docVector = {}
            title_vector = [0]*len(self.title_words_list)
            for word in doc['title']:
                title_vector[self.title_indexes[word]] = title_vector[self.title_indexes[word]]+1
            body_vector = [0]*len(self.body_words_list)
            for word in doc['body']:
                body_vector[self.body_indexes[word]] = body_vector[self.body_indexes[word]]+1
            docVector['title'] = title_vector
            docVector['body'] = body_vector
            docVector['id'] = doc['id']
            self.docVectors.append(docVector)    
    

    def query(self, search_query, total_clicks, song_clicks):
        query_title_vector = [0]*len(self.title_words_list)
        for word in search_query:
            if word in self.title_indexes:
                query_title_vector[self.title_indexes[word]] = query_title_vector[self.title_indexes[word]]+1

        query_body_vector = [0]*len(self.body_words_list)
        for word in search_query:
            if word in self.body_indexes:
                query_body_vector[self.body_indexes[word]] = query_body_vector[self.body_indexes[word]]+1
        result = []
        for docVector in self.docVectors:
            title_cosine = self.calculateCosine(query_title_vector, docVector['title'])
            body_cosine = self.calculateCosine(query_body_vector, docVector['body'])
            weighted_cosine = 0.4*title_cosine + 0.5*body_cosine
            # if docVector['id'] == 36 or docVector['id'] == 97:
            #     print(title_cosine, body_cosine, docVector['id'])
            if weighted_cosine != 0.0:
                if total_clicks != 0:
                    weighted_cosine = weighted_cosine + 0.1*(song_clicks[docVector['id']]/total_clicks)
                result.append({'weighted_cosine':weighted_cosine, 'id':docVector['id']})
        result = sorted(result, key = lambda i: -i['weighted_cosine'])
        return result

    def calculateCosine(self, query_vector, doc_vector):
        determinant_q = 0.0
        for val in query_vector:
            determinant_q = determinant_q+val*val
        determinant_q = math.sqrt(determinant_q)    
        determinant_v = 0.0
        for val in doc_vector:
            determinant_v = determinant_v + val*val 
        determinant_v = math.sqrt(determinant_v)
        numerator = 0.0
        for x in range(len(doc_vector)):
            numerator = numerator+query_vector[x]*doc_vector[x]
        denominator = determinant_q*determinant_v    
        if denominator == 0.0:
            return 0.0
        cosine = numerator/denominator
        return cosine      

