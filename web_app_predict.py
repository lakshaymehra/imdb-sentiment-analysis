from flask import Flask, request, jsonify, render_template
app = Flask(__name__) #, template_folder='C:/Users/mehra/OneDrive/Documents/GitHub/imdb-sentiment-analysis')
import numpy as np
import keras

model = keras.models.load_model("imdb_reviews.h5")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    import tensorflow_datasets as tfds
    imdb, info = tfds.load("imdb_reviews", with_info=True, as_supervised=True)
    import numpy as np

    train_data, test_data = imdb['train'], imdb['test']

    training_sentences = []
    training_labels = []

    testing_sentences = []
    testing_labels = []

    # str(s.tonumpy()) is needed in Python3 instead of just s.numpy()
    for s, l in train_data:
        training_sentences.append(str(s.numpy()))
        training_labels.append(l.numpy())

    for s, l in test_data:
        testing_sentences.append(str(s.numpy()))
        testing_labels.append(l.numpy())

    vocab_size = 10000
    max_length = 120
    trunc_type = 'post'
    oov_tok = "<OOV>"

    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences

    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
    tokenizer.fit_on_texts(training_sentences)

    new_review = [x for x in request.form.values()]

    new_testing_sequence = tokenizer.texts_to_sequences(new_review)
    new_testing_padded = pad_sequences(new_testing_sequence, maxlen=max_length)
    new_a = np.array(np.array(new_testing_padded))

    prediction = model.predict(new_a)[0]
    print(prediction)
    if prediction < 0.5:
        sentiment = "NEGATIVE"
    else:
        sentiment = "POSITIVE"

    return render_template('index.html', prediction_text='The review has a {} sentiment'.format(sentiment))


if __name__ == "__main__":
    # FOR DOCKER:
    app.run(host ='0.0.0.0', port = 5001,debug=True)

    # FOR FLASK:
    # app.run(port=5001, debug=True)


# FOR DOCKER:
# bash build_docker.sh
# bash run_docker.sh
# VISIT LINK : http://192.168.99.100:5001/

# FOR FLASK:
# python web_app_predict.py
# VISIT LINK : http://127.0.0.1:5001/