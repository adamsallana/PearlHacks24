from distutils.log import debug 
from fileinput import filename 
from flask import *  
app = Flask(__name__)   
  
@app.route('/')   
def main():   
    return render_template("index.html")   

@app.route('/upload')   
def upload():   
    return render_template("uploadnotes.html") 



@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save('documents/'+f.filename)   
        return render_template("totesdidit.html", name = f.filename)   

# import os

# # @app.route('/searchresults')   
# # def results():   
# #         folderPath = r"C:\Users\Allana\Dev\PearlHacks24\PearlHacks24\PearlHacks24-1\documents"
# #         documentsList = []
# #         for x in os.scandir(folderPath):
# #              documentsList.append[x.name]
# #         return render_template("searchnotes-res.html", names = documentsList)   

# folderPath = r"C:\Users\Allana\Dev\PearlHacks24\PearlHacks24\PearlHacks24-1\documents"

# def getFiles():
#     def fObjFromScan(x):
#         # return file information for rendering
#         return {'name': x.name,
#                 'relPath': os.path.relpath(x.path, folderPath).replace("\\", "/")}
#     fileObjs = [fObjFromScan(x) for x in os.scandir(folderPath)]

#     return render_template('files.html.j2', data={'files': fileObjs})


if __name__ == '__main__':   
    app.run(debug=True)

