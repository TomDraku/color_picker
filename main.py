from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
import os
from sklearn.cluster import KMeans

"""
def top_colors(img_path):
    img = Image.open(img_path)
    img_array = np.array(img)
    unique, counts = np.unique(img_array.reshape(-1, img_array.shape[2]), axis=0, return_counts = True)
    top_colors = unique[np.argsort(counts)[::-1][:10]]
    return top_colors
"""
def top_colors(img_path):
    img = Image.open(img_path)
    img_array = np.array(img)
    x = img_array.reshape(-1, img_array.shape[2])
    kmeans = KMeans(n_clusters=10, random_state=0).fit(x)
    top_colors = kmeans.cluster_centers_
    counts = np.unique(kmeans.labels_,return_counts=True)[1]
    top_colors = top_colors[np.argsort(counts)[::-1]]
    return top_colors
 

app = Flask(__name__)

# Path to the upload folder
upload_folder = os.path.join('static', 'uploads')

print(upload_folder)

# saving path to the upload folder as a variable
app.config['UPLOAD'] = upload_folder



@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      file = request.files['img']
      filename = secure_filename(file.filename)
      for filename in os.listdir(app.config['UPLOAD']):
         file_path = os.path.join(app.config['UPLOAD'], filename)
         
         # check if the file is a regular file (not a directory)
         if os.path.isfile(file_path):
            
            # delete the file
            os.remove(file_path)   
      file.save(os.path.join(app.config['UPLOAD'], filename))
      img = os.path.join(app.config['UPLOAD'], filename)
      my_colors = top_colors(img)
      return render_template('index.html', img=img, my_colors=my_colors)
   return render_template('index.html')


   

















if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)