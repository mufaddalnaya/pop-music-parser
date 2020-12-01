from . import Documents, stopwords

class WordProcess:
    def __init__(self):
        # Processing the Documents
        # Step-1 Removing puncuations and special characters such as newline
        # Step-2 Tokenization
        # Step-3 Conerting to lowercase
        # Step-4 Removing Stop words
        # Step-5 Stemming

        self.doc = self.getDocs()

        self.freq_dist = []
        self.processed_doc = []
        for topic in self.doc:
            new_doc = []
            for docs in topic: 
                lyrics = {}
                lyrics['title'] = self.processString(docs['lyrics'])
                lyrics['body'] = self.processString(docs['body'])
                lyrics['id'] = docs['id']
                new_doc.append(lyrics)
            self.processed_doc.append(new_doc)  

    def processString(self, docs):
        splitted_doc = self.split(self.remove_punc(docs.replace("\n", "").replace("\xa0","").replace("\t","")))
        lowercase_doc = self.lower_case(splitted_doc)
        stop_word_removed = self.remove_stopwords(lowercase_doc)
        stemming_doc = self.stem(stop_word_removed)
        return stemming_doc

    # Removing punctuations in string 
    def remove_punc(self, str):
        punc = '''!()-[];:'",<>./?@#$%^&*_~'''
        for ele in str:  
            if ele in punc:  
                str = str.replace(ele, "")  
        return str

    def stem(self, words):
        return_lst = []
        for word in words:
            for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
                if word.endswith(suffix):
                    word = word[:-len(suffix)]
            return_lst.append(word)
        return return_lst

    def split(self, string):
        result_list = []
        ptr1 = 0
        for index, char in enumerate(string):
            if char == " ":
                result_list.append(string[ptr1:index])
                ptr1 = index + 1
        if ptr1 == 0:
            return [string]
        result_list.append(string[ptr1:index + 1])
    
        return result_list

    def lower_case(self, words):
        result_list = []
        for word in words:
            result_list.append(word.lower())
        
        return result_list

    def remove_stopwords(self, words):
        stopwords = self.get_stopwords()
        result_list = []
        for word in words:
            if word not in stopwords:
                result_list.append(word)
        
        return result_list

    def get_stopwords(self):
        data = stopwords.getStopwords()  
        stop_words = [] 
        for sub in data: 
            stop_words.append(sub.replace("\n", ""))     
        stop_words = set(stop_words)

        return stop_words

        

    def getDocs(self):
        return Documents.getDocs()

    