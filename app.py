from flask import Flask,request,render_template
import os
import csv
import tensorflow as tf

#firebase:
'''
import firebase_admin
from firebase_admin import credentials, firestore
'''


app=Flask(__name__)

#ML model:
#model=tf.keras.models.load_model('efficientnetb3-Eye Disease-96.19.h5')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/1session',methods=['POST','GET'])
def session1():
    return render_template('session1.html')

@app.route('/2session',methods=['POST','GET'])
def session2():
    return render_template('session2.html')


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        first_name=str(request.form['First Name'])
        last_name=str(request.form['Last Name'])

        age=int(request.form['age'])
        occupation=str(request.form.get('occupation'))
        gender=str(request.form['gender'])
        prev_eye_surgery=str(request.form.get('prev_eye_surgery'))
        existing_ailments=str(request.form.get('existing_ailments'))
        high_bp=str(request.form.get('high_bp'))
        Diabetes=request.form.get('Diabetes')
        chief_complaints=request.form.getlist('Chief complaints')

        contact=int(request.form['contact'])
        email=str(request.form.get('email'))
        relative_contact=str(request.form.get('relative_contact'))
        existing_doctor=str(request.form.get('existing_doctor'))
        family_history=str(request.form.get('family_history'))
        Glaucoma=str(request.form.get('Glaucoma'))
        Macular_Degeneration=str(request.form.get('Macular Degeneration'))

        hosp_name=str(request.form['hosp'])
        fundus=request.files['fundus']

        # prediction=model.predict(fundus)

        data=[first_name,last_name,age,occupation,gender,prev_eye_surgery,existing_ailments,high_bp,Diabetes,chief_complaints,contact,email,relative_contact,existing_doctor,family_history,Glaucoma,Macular_Degeneration,hosp_name]
        
       
            
        #main folderL
        # Base folder:
        base_folder='C:/Imai_data'
        os.makedirs(base_folder,exist_ok=True)


        #hosp folder:
        hosp_folder=os.path.join(base_folder,hosp_name)
        os.makedirs(hosp_folder,exist_ok=True)

        #image folder path:
        img_folder=os.path.join(hosp_folder,'fundus_images')
        os.makedirs(img_folder,exist_ok=True)
        #adding image
        file_path=os.path.join(img_folder,fundus.filename)
        fundus.save(file_path)


        #csv file path:
        csv_file=os.path.join(hosp_folder,'data.csv')

        #writing data into csv file
        file_exists=os.path.isfile(csv_file)
        with open(csv_file,mode='a',newline='') as file:
            writer=csv.writer(file)
            if not file_exists:
                writer.writerow(['First Name','Last Name','Age','Occupation','Gender','Previous eye surgeries','Existing Ailments','High B.P','Diabetes','Chief Complaints','Contact',"email",'relative_contact','existing_doctor','family_history','Glaucoma','Macular_Degeneration','hosp_name','Hospital Name'])
            writer.writerow(data)
        return render_template('submit_page.html')
    else:
        return 'some issue'
    


@app.route('/diagnosis',methods=['POST','GET'])
def diagnosis():
    if request.method=='POST':
        if request.form.get('docid')=='doc123':
            return'DOCTOR VERFIED' 
        else:
            return 'WRONG DOCTOR ID'
    else:
        return 'couldnt find data'


            

'''
#already done!
def session(name):
    if name=='1session':
        return render_template('session1.html')
    elif name=='2session':
        return render_template('session2.html')
    elif name=='submit':
        if request.method=='POST':
            name_patient=str(request.form['name'])
            age=int(request.form['age'])
            gender=str(request.form['gender'])
            contact=int(request.form['contact'])
            hosp_name=str(request.form['hosp'])
            fundus=request.files['fundus']
            data=[name_patient,age,gender,contact,hosp_name]
            

            #main folderL
            # Base folder:
            base_folder='C:/Imai_data'
            os.makedirs(base_folder,exist_ok=True)


            #hosp folder:
            hosp_folder=os.path.join(base_folder,hosp_name)
            os.makedirs(hosp_folder,exist_ok=True)

            #image folder path:
            img_folder=os.path.join(hosp_folder,'fundus_images')
            os.makedirs(img_folder,exist_ok=True)
            #adding image
            file_path=os.path.join(img_folder,fundus.filename)
            fundus.save(file_path)


            #csv file path:
            csv_file=os.path.join(hosp_folder,'data.csv')

            #writing data into csv file
            file_exists=os.path.isfile(csv_file)
            with open(csv_file,mode='a',newline='') as file:
                writer=csv.writer(file)
                if not file_exists:
                    writer.writerow(['Patient Name','Age','Gender','Contact','Hospital Name'])
                writer.writerow(data)
            return render_template('submit_page.html')




            
        else:
            return'another issue '
    
    else:
        return 'some issue '
    
    
    


# @app.route('/<name>',methods=['POST','GET'])

'''




if __name__ == '__main__':
    app.run(debug=True)
