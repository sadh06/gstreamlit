import pandas as pd
from pycaret.classification import *
import streamlit as st

import streamlit as st
import pandas as pd

def app():
    import numpy as np
    from importlib import import_module
    import joblib

    st.title('Streamlit Example')

    st.write("Titanic Dataset")

    #classifier_name = st.text_input("Classifier_name")

    file_upload = st.file_uploader("Upload csv file for train", type=["csv"])

    if file_upload is not None:
        train = pd.read_csv(file_upload)

    """file_upload = st.file_uploader("Upload csv file for Y_train", type=["csv"])

    if file_upload is not None:
        Y_train= pd.read_csv(file_upload) """

    

    if st.button("Train"):

        train["Survived"]=train["Survived"].apply(lambda x:"Survived" if x==1 else "Dead")
        s=setup(train,target = 'Survived',
             numeric_imputation = 'mean',
             categorical_features = ['Sex','Embarked'], 
             numeric_features=["SibSp","Parch","Pclass"],
             ignore_features = ['Name','Ticket','Cabin'],
             silent = True,
             log_experiment = True, 
             experiment_name = 'titanic')
        g_boost  = create_model('gbc') 
        tuned_gb = tune_model(g_boost)
        rand_for=create_model('rf') 
        log_reg=create_model('lr')
        lgbm=create_model('lightgbm')
        adabcf=create_model('ada')
        



        save_model(g_boost , 'deploy_gboost')
        save_model(rand_for,'deploy_rand_for')
        
        save_model(log_reg,'deploy_log_reg')
        save_model(lgbm,'deploy_log_lgbm')
        save_model(adabcf,'deploy_log_ada')


        #model = create_model(model_name)
       
        #filename = model_name + "trained.sav"
        #joblib.dump(model,filename)

        """directory = os.path.abspath(os.getcwd())
        with open(os.path.join(directory,model_name),"wb") as f: 
          f.write(model_name.getbuffer())"""
        st.text("Models saved")


    

    

    
  
"""
def app():
    st.title('PYCARET')
    st.write('Welcome to pycaret training')

    #train = pd.read_csv('train.csv')
    #test = pd.read_csv('test.csv')
    file_upload = st.file_uploader("Upload csv file for X_train", type=["csv"])

    if file_upload is not None:
        train = pd.read_csv(file_upload)

        train["Survived"]=train["Survived"].apply(lambda x:"Survived" if x==1 else "Dead")
        clf1 = setup(data = train, target='Survived'
               
                )
    if st.button("Train"):
        model_name = classifier_name.split(".")
        model = create_model(model_name)
        
        filename = model_name + "trained.sav"
        joblib.dump(model,filename)

        directory = os.path.abspath(os.getcwd())
        with open(os.path.join(directory,model_name),"wb") as f: 
          f.write(model_name.getbuffer())
        st.text("Model saved")"""
    