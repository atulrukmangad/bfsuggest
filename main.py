from flask import Flask, render_template
from random import randint
app = Flask(__name__)
day1 = "Random"
day2 = "Random"
@app.route('/')
def mainfunction():
    bflist = ["Poha","Upma","Shevai Upma","Daliya","Dhokla","Sandwich","White Dhokla","Dhirde","Sanza","Ukarpendi","Thalipeeth","Plain Parathe","Methi che muthe","Idli","Appe"]
    vid_link = ["https://youtu.be/8LwYrE7PaC0","https://youtu.be/SogcWMwjxS0","https://youtu.be/s7dl4Zay7OQ","https://youtu.be/rUWgTPPHJBw","https://youtu.be/OIK96k4rghs","https://youtu.be/4nbJsRIE_5k","https://youtu.be/hrEaZUCGbSM","https://youtu.be/7DKAoseLVXA","https://youtu.be/D3t4rBB4kSY","https://youtu.be/b99HhTZz83Y","https://youtu.be/INoP1X5OaDk","https://youtu.be/Y9KwgOjdsWw","https://youtu.be/du7l-18_UNk","https://youtu.be/eBNt1ev0eKM","https://youtu.be/X2z4_ge1CvY"]
    generate = True
    global day1
    global day2
    while generate:
        answer = bflist[randint(0,14)]
        if answer == day1 or answer == day2:
            generate = True
        else:
            generate = False
    day2 = day1
    day1 = answer
    return render_template('main.html', answer=answer, recipe_vid=vid_link[bflist.index(answer)])


if __name__ == '__main__':
    app.run()