# SearchEngine

Search Engine web application created using Python Django Framework.<br>
If you are using linux ecosystem you can easily run the project using the command : "bash script.sh" in the project folder.<br>

The algorithm used for searching queries is based on the Cosine Similarity between documents. The database contains 10 documents 5 based on the Topic Chess and 5 based on the Topic Covid 19. The Documents are already added in the project and can be updated from Documents.py file inside search directory.<br>

Documentation of Specific classes:
<ol>
<l1><b>QueryProcessing.py : </b> It containes the algorithm for calulating cosine similairty of the query with the corpus.</li>
<l1><b>WordProcess.py : </b> It contains the code for processing the document as well as the queries. It consists of 5 steps as mentioned in the comments of the file.</li>
<l1><b>Documents.py : </b> Contains corpus of 10 documents.</li>
</ol>

The Projects contains 2 routes, First one is the homepage("/") and the second is the search("/search").

Project Homepage<br>
![Homepage image](https://github.com/mufaddalnaya/SearchEngine/blob/master/Homepage.png?raw=true)

