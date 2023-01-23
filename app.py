from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "O Senhor dos Anéis - A Sociedade do Anel",
        "author": "J.R.R Tolkien"
    },
    {
        "id": 2,
        "title": "Harry Potter e a Pedra Filosofal",
        "author": "J.K Howling"
    },
    {
        "id": 3,
        "title": "Hábitos Atômicos",
        "author": "James Clear"
    }
]


#Get all
@app.route('/books', methods=['GET'])
def getBooks():
    return jsonify(books)
    
    
#Get by ID
@app.route('/books/<int:id>', methods=['GET'])
def getBookById(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)        
            
            
#Create
@app.route('/books/create', methods=['POST'])
def createBook():    
    new_book = request.get_json()
    books.append(new_book)
    
    return jsonify(books)            
           
            
#Edit
@app.route('/books/<int:id>', methods=['PUT'])
def editBookById(id):
    modified_book = request.get_json()
    for i, book in enumerate(books):
        if book.get('id') == id:
            books[i].update(modified_book)
            return jsonify(books[i])
    
    
#Delete
@app.route('/books/<int:id>', methods=['DELETE'])
def deleteBookById(id):
    for i, book in enumerate(books):
        if book.get('id') == id:
            del books[i]
    
    return jsonify(books)
        

app.run(port=5000,host='localhost',debug=True)