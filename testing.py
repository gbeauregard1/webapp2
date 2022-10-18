from flask import Blueprint, render_template, request, flash, redirect, url_for
from matplotlib.pyplot import text
import requests
import os
import openai

openai.api_key = "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"

#import settings



testing = Blueprint('testing', __name__)

actor1 = ''

@testing.route('/', methods=['GET', 'POST'])

def enter():
    if request.method == 'POST':
        global actor1, actor2, director
        actor1 = request.form.get('actor1')
        actor2 = request.form.get('actor2')
        director = request.form.get('director')
        genre = request.form.get('genre')

        #text = str(tag)
        nada = ''

        # if len(username) < 2:
        #     print("bad")
        #     pass
        if actor1 == nada:
            flash('Please input an actor.', category='error')
        else:
            #add user to database
            response_title = openai.Completion.create(
                model="text-davinci-002",
                prompt="Write a movie title for a "+genre+" starring"+actor1 + "and "+actor2+" directed by "+director+"\n\n",
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            response_tagline = openai.Completion.create(
                model="text-davinci-002",
                prompt="Write a movie tagline for a "+genre+" starring"+actor1 + "and "+actor2+" directed by "+director+"\n\n",
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            response_summary = openai.Completion.create(
                model="text-davinci-002",
                prompt="Write a movie summary for a "+genre+" starring"+actor1 + "and "+actor2+" directed by "+director+"\n\n",
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            
            return("Movie Title:" + response_title.choices[0].text + "\n" + "Movie Tagline:" + response_tagline.choices[0].text + "\n" + "Movie Tagline:" + response_summary.choices[0].text + "\n")
            #return actor1
            #flash('Welcome', category='success')
            #return redirect(url_for('views.home'))
            #return render_template("next.html")

    return render_template("enter.html")

# def getFirst():
#     if request.method == 'POST':
#         global actor1
#         actor1 = request.form.get('actor1')

#         #text = str(tag)
#         nada = ''

#         if actor1 == nada:
#             flash('Please input an actor.', category='error')
#         else:
#             #add user to database
#             return actor1
#     return render_template("enter.html")


# def move():
#     print(actor1)
#     flash('Welcome', category='success')
#     #return redirect(url_for('views.home'))
#     return render_template("next.html")