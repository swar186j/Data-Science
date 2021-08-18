import os
from flask import Flask, render_template, request, send_file
import cv2 
from werkzeug.utils import secure_filename

app= Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

global content

@app.route('/', methods=['POST'])
def create():
    imagefile= request.files['imagefile']
    image_path="./images/" + imagefile.filename
    img= imagefile.save(image_path)
    image= cv2.imread(image_path)
    if request.form['submit_button'] == 'Sketch':
        gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        inverted_image= 255-gray_image
        blurred= cv2.GaussianBlur(inverted_image, (21,21), 0)
        inverted_blurred= 255-blurred
        pencil_sketch= cv2.divide(gray_image, inverted_blurred, scale= 256.0)
        cv2.imwrite("sketch.png", pencil_sketch)
        content='sketch.png'
        return send_file(content,as_attachment=True)
        
        #cartoonize
    elif request.form['submit_button'] == 'Cartoon':
        gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred= cv2.GaussianBlur(gray_image, (3,3), 8)
        edges = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5,5)
        cartoon = cv2.bitwise_and(image, image, mask = edges)
        cv2.imwrite("cartoon.png", cartoon)
        content='cartoon.png'
        return send_file(content,as_attachment=True)

    elif request.form['submit_button'] == 'Oil':
        oil = cv2.xphoto.oilPainting(image, 7, 1)
        cv2.imwrite("oil.png",oil)
        content='oil.png' 
        return send_file(content,as_attachment=True)

    elif request.form['submit_button'] == 'Water':
        water=cv2.stylization(image, sigma_s=60, sigma_r=0.6)
        cv2.imwrite("water.png",water)
        content='water.png' 
        return send_file(content,as_attachment=True)

    elif request.form['submit_button'] == 'Gray':
        gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("gray.png",gray_image)
        content='gray.png' 
        return send_file(content,as_attachment=True)

    elif request.form['submit_button'] == 'Blur':
        blurred=cv2.blur(image,(10,10))
        cv2.imwrite("blur.png",blurred)
        content='blur.png'
        return send_file(content,as_attachment=True)
    
    return render_template('home.html')


if __name__=="__main__":
    app.run(debug=True)
