import os
from flask import Flask, jsonify, request
from models import db, Quote
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

@app.route('/api/quotes', methods=['GET'])
def return_all():
    quotes = Quote.query.all()
    quote_list = []
    for quote in quotes:
        curr_quote = {}
        curr_quote['id'] = quote.id
        curr_quote['time_created'] = quote.time_created
        curr_quote['text'] = quote.text
        curr_quote['user_id'] = quote.user_id
        quote_list.append(curr_quote)
    return jsonify(quotes=quote_list)

@app.route('/api/new', methods=['POST'])
def create_new():
    text = request.form['text']
    user_id = int(request.form['user_id'])

    if text and user_id:
        quote = Quote(text, user_id)
        db.session.add(quote)
        db.session.commit()
        # return success json
    else:
        # return error json
        return

@app.route('/api/update', methods=['POST'])
def update():
    quote_id = int(request.form['id'])

    text = request.form['text']
    user_id = int(request.form['user_id'])

    if quote_id:
        curr_quote = Quote.query.filter_by(id=quote_id).first()
        if text:
            curr_quote.text = text
        if user_id:
            curr_quote.user_id = user_id
        # return success json
    else:
        # return error json
        return

@app.route('/api/delete/<int:quote_id>', methods=['DELETE'])
def delete(quote_id):
    quote = Quote.query.filter_by(id=quote_id).first()
    db.session.delete(quote)
    db.session.commit()

    #return success json

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    db.init_app(app)
    app.run(host='0.0.0.0', port=port, debug=True)