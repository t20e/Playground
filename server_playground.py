from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/play')
def box():
    return render_template("index.html",boxes=3,color ="blue")

@app.route('/play/<int:boxes>')
def boxes(boxes):
    return render_template("index.html",boxes=boxes, color ="blue")

@app.route('/play/<int:boxes>/<color>')
def boxes_color(boxes,color):
    return render_template("index.html",boxes = boxes,color =color)



if __name__ =="__main__":
    app.run(debug=True)