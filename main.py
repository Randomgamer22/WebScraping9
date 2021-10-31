from flask import Flask, jsonify, request
import csv

all_articles = []

liked_articles = []
unliked_articles = []
unwatched_movies = []

with open('articles.csv', 'r', encoding = 'UTF8') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    all_articles = data[1:]

app = Flask(__name__)

@app.route("/get_article")
def get_articles():
    article_data = {
                'title': all_articles[0][13]
            }

    return jsonify(
            {
                'data': article_data,
                'message': 'Success'
            }
        ), 200

@app.route("/liked_articles", methods = ["POST"])
def liked_articles():
    movie = all_articles[0]
    liked_articles.append(movie)
    all_articles.pop(0)

    return jsonify (
                {
                    'message': 'Success'
                }
            ), 200


@app.route("/unliked_articles", methods = ["POST"])
def unliked_articles():
    movie = all_articles[0]
    unliked_articles.append(movie)
    all_articles.pop(0)

    return jsonify (
                {
                    'message': 'Success'
                }
            ), 200

if __name__ == "__main__":
    app.run()



