import pandas as pd
import streamlit as st


def app():
    import joblib
    st.title('Streamlit Example')
    st.write("Predict your results !!")

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Multiple inputs", "Single input"))

    if add_selectbox == "Single input":
        st.write("Give your values to Predict")
        Pclass = st.number_input('P Class', 1, 3)
        Sex = st.selectbox('Sex', ['male', 'female'])
        Age = st.number_input('Age', min_value=1, max_value=100, value=25)
        Fare = st.slider('Fare', 0, 600)
        Cabin = st.selectbox('Cabin', [0, 0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8]) 
        Embarked = st.selectbox('Embarked', ['S', 'C', 'Q'])
        FamilySize = st.slider('Family size', 1, 11)
            
        if Sex == "male":
            Title = st.selectbox('Title', ['Mr', 'Master', 'Others'])
        else:
            Title = st.selectbox('Title', ['Ms', 'Mrs', 'Others'])

        input_dict = {
                'Pclass': Pclass,
                'Sex': Sex,
                'Age': Age,
                'Fare': Fare,
                'Cabin': Cabin,
                'Embarked': Embarked,
                'Title': Title,
                'FamilySize': FamilySize}
        input_df = pd.DataFrame([input_dict])
        

        dic_sex = {"male": 0, "female": 1}
        input_df["Sex"] = input_df["Sex"].map(dic_sex)

        title_mapping = {'Mr': 0, 'Ms': 1, 'Mrs': 2, 'Master': 3, 'Others': 4}
        input_df['Title'] = input_df['Title'].map(title_mapping)

        embarked_mapping = {"S": 0, "C": 1, "Q": 2}
        input_df['Embarked'] = input_df['Embarked'].map(embarked_mapping)

        family_mapping = {
            1: 0,
            2: 0.4,
            3: 0.8,
            4: 1.2,
            5: 1.6,
            6: 2,
            7: 2.4,
            8: 2.8,
            9: 3.2,
            10: 3.6,
            11: 4}
        input_df['FamilySize'] = input_df['FamilySize'].map(family_mapping)

        if Fare <= 17:
            input_df["Fare"] = 0
        elif (Fare > 17 & Fare <= 30):
            input_df["Fare"] = 1
        elif (Fare > 30 & Fare <= 100): 
            input_df["Fare"] = 2
        elif (Fare > 100):
            input_df["Fare"] = 3

        if Age <= 16:
            input_df["Age"] = 0
        elif (Age > 16 and Age <= 25):
            input_df["Age"] = 1
        elif (Age > 25 and Age <= 35):
            input_df["Age"] = 2
        elif (Age > 35 and Age <= 45):
            input_df["Age"] = 3
        elif (Age > 45):
            input_df["Age"] = 4

        print(input_df)

        st.dataframe(input_df)

        file_upload = st.file_uploader(
            "Upload sav file for prediction", type=["sav"])

        if file_upload is not None:

            load_clf = joblib.load(file_upload)
            output = load_clf.predict(input_df)
            if output == 0:
                output = "Not survived"
            else:
                output = "Survived"

            if st.button("Predict"):
                st.success('The output is {} '.format(output))

    else:
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
           input_df = pd.read_csv(file_upload)
           
           dic_sex = {"male": 0, "female": 1}
           input_df["Sex"] = input_df["Sex"].map(dic_sex)

           title_mapping = {'Mr': 0, 'Ms': 1, 'Mrs': 2, 'Master': 3, 'Others': 4}
           input_df['Title'] = input_df['Title'].map(title_mapping)

           embarked_mapping = {"S": 0, "C": 1, "Q": 2}
           input_df['Embarked'] = input_df['Embarked'].map(embarked_mapping)
           
           family_mapping = {
                            1: 0,
                            2: 0.4,
                            3: 0.8,
                            4: 1.2,
                            5: 1.6,
                            6: 2,
                            7: 2.4,
                            8: 2.8,
                            9: 3.2,
                            10: 3.6,
                            11: 4}
           input_df['FamilySize'] = input_df['FamilySize'].map(family_mapping)

           input_df.loc[input_df['Fare'] <= 17, 'Fare'] = 0
           input_df.loc[(input_df['Fare'] > 17) & (input_df['Fare'] <= 30), 'Fare'] = 1
           input_df.loc[(input_df['Fare'] > 30) & (input_df['Fare'] <= 100), 'Fare'] = 2
           input_df.loc[input_df['Fare'] > 100, 'Fare'] = 3

           input_df.loc[input_df['Age'] <= 16, 'Age'] = 0
           input_df.loc[(input_df['Age'] > 16) & (input_df['Age'] <= 25), 'Age'] = 1
           input_df.loc[(input_df['Age'] > 25) & (input_df['Age'] <= 35), 'Age'] = 2
           input_df.loc[(input_df['Age'] > 35) & (input_df['Age'] <= 45), 'Age'] = 3
           input_df.loc[input_df['Age'] > 45, 'Age'] = 4
                
           
           st.dataframe(input_df)

           file_upload = st.file_uploader(
                    "Upload sav file for prediction", type=["sav"])

           if file_upload is not None:

                load_clf = joblib.load(file_upload)
                output = load_clf.predict(input_df)
                out = pd.DataFrame({"Predictions": output})
                result = pd.concat([input_df, out], axis=1)
                result.to_csv("sample.csv")
                path = '/Users/Dell Laptop/Python/env'
                full_path = path + "/ " + 'sample.csv'

                if st.button("Predict"):
                    st.success('The output is saved as csv in')
                    st.write(full_path)
