from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    genre = request.args['genre']
    age = request.args['age']
    if genre == 'Action' and age == 'older':
        reply = "You should watch Indiana Jones"
        movimage = "/static/Indiana.jpg"
    elif genre == 'Action' and age == 'newer':
        reply = "You should watch Borderlands"
        movimage = "/static/Borderlands.jpg"
    elif genre == 'Horror' and age == 'older':
        reply = "You should watch Halloween"
        movimage = "/static/Halloween.jpg"
    elif genre == 'Horror' and age == 'newer':
        reply = "You should watch Nope"
        movimage = "/static/Nope.jpg"
    elif genre == 'Sci-Fi' and age == 'older':
        reply = "You should watch Alien"
        movimage = "/static/Alien.jpg"
    elif genre == 'Sci-Fi' and age == 'newer':
        reply = "You should watch Interstellar"
        movimage = "/static/Interstellar.jpg"
    elif genre == 'Fantasy' and age == 'older':
        reply = "You should watch Lord of the Rings"
        movimage = "/static/LOTR.jpg"
    else:
        reply = "You should watch Dune"
        movimage = "/static/Dune.jpg"
    return render_template('response.html', response = reply, image = movimage)

if __name__=="__main__":
    app.run(debug=True)
