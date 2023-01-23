from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'O Senhor dos Anéis - A Sociedade do Anel',
        'author': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'title': 'Harry Potter e a Pedra Filosofal',
        'author': 'J.K Howling'
    },
    {
        'id': 3,
        'title': 'Hábitos Atômicos',
        'author': 'James Clear'
    }
]


#Get all
@app.route('/books', methods=['GET'])
def getBooks():
    return jsonify(books)
    
#Consultar por ID
@app.route('/books/<int:id>', methods=['GET'])
def getBookById(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)        
            
#Editar
#Excluir


app.run(port=5000,host='localhost',debug=True)