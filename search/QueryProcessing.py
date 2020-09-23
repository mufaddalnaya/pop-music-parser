import math  

class QueryProcessing:

    def __init__(self, topics):
        self.docs = []
        for topic in topics:
            for doc in topic:
                self.docs.append(doc)
            
        self.words = set()
        for doc in self.docs:
            for word in doc:
                self.words.add(word)
        self.words_list = []
        for word in self.words:
            self.words_list.append(word)
        self.indexes = {}
        for idx, word in enumerate(self.words_list):
            self.indexes[word] = idx
        self.docVectors = []        
        for doc in self.docs:
            vector = [0]*len(self.words_list)
            for word in doc:
                vector[self.indexes[word]] = vector[self.indexes[word]]+1
            self.docVectors.append(vector)

    def query(self, search_query):
        query_vector = [0]*len(self.words_list)
        for word in search_query:
            if word in self.indexes:
                query_vector[self.indexes[word]] = query_vector[self.indexes[word]]+1
        result = []
        for idx, docVector in enumerate(self.docVectors):
            cosine = self.calculateCosine(query_vector, docVector)
            if cosine != 0.0:
                result.append({'cosine':cosine, 'doc':self.docs[idx]})
        result = sorted(result, key = lambda i: -i['cosine'])
        return result            

    def calculateCosine(self, query_vector, doc_vector):
        dominant_q = 0.0
        for val in query_vector:
            dominant_q = dominant_q+val*val
        dominant_q = math.sqrt(dominant_q)    
        dominant_v = 0.0
        for val in doc_vector:
            dominant_v = dominant_v + val*val 
        dominant_v = math.sqrt(dominant_v)
        numerator = 0.0
        for x in range(len(doc_vector)):
            numerator = numerator+query_vector[x]*doc_vector[x]
        if dominant_q == 0.0 or dominant_v == 0.0:
            return 0.0
        cosine = numerator/(dominant_q*dominant_v)
        return cosine      

