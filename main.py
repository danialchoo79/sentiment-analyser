import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    score = ((sid.polarity_scores(str(text))))['compound']  # The normalized compound score which calculates the sum of all lexicon ratings and takes values from -1 to 1

    if (score > 0):
        label = 'This sentiment in the sentence is positive'
    elif (score == 0):
        label = 'This sentiment in the sentence is neutral'
    else:
        label = 'This sentiment in the sentence is negative'

    return(render_template('index.html',variable=label))

if __name__ == '__main__':
    app.run(port='8088', threaded=False, debug=True)
