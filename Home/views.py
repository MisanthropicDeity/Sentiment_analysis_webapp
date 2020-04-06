from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotModified
from . forms import NameForm
from . models import data
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

max_length = 100
trunc_type = 'post'
padding_type='post'
prob = -1
news = ''


def get_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)

		if form.is_valid():
			return HttpResponse('Thanks')
	else:
		form =NameForm()

	return render(request, 'name.html' , {'form':form})
	

def feed(request):
    
    return render(request, 'feed.html')

def fform(request):

    sub = data(data = request.POST["message"])

    sub.save()
    print(sub.data)
    sentence = [sub.data]
    print(type(sentence))
    with open('/home/deity/Documents/django/sentiment_analysis/tokenizer.pickle', 'rb') as handle:
    	tokenizer = pickle.load(handle)
    model = tf.keras.models.load_model('/home/deity/Documents/sentiment_analysis/mymodel')

    #tokenizer = Tokenizer(num_words = 10000, oov_token = oov_token)
    sequences = tokenizer.texts_to_sequences(sentence)
    padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    prediction = model.predict(padded)
    print("prediction")
    print(prediction)
    # prob1 = prediction[0]
    # prob2 = prediction[1]
    # print (prpb1)
    # print (prob2)
    prob = prediction[0][0]
    prob =prob*100
    news = sub.data
    return HttpResponse('<h1> the following news headline : {} has {} percent probablity of being a sarcastic news </h1>'.format(news,prob))


def thank(request):
    
    return render(request, 'thank.html',{'probablity':prob,'headline':news})