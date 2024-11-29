#Titanic Survival Prediction App Development
import streamlit as st
import pickle

#Set the title and an image for the web app
st.title("Welcome to Daren's Survival Prediction App")
st.image('image.png')

#Load the pre-trained model
with open('titanicpickle.pkl', 'rb') as pickle_file:
    pickle_load_file = pickle.load(pickle_file)

#Function to make predictions
def PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    prediction = pickle_load_file.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])
    print(prediction) #0/1
    return prediction

def main():
    st.title('Titanic Prediction App!')
    #The following code creates the input fields, that will be used by the user
    #for data entry for prediction
    Pclass = st.text_input('Passenger Class')
    Sex = st.text_input('Sex')
    Age = st.text_input('Age')
    SibSp = st.text_input('Sibling/Spouse')
    Parch = st.text_input('Parent/Child')
    Fare = st.text_input('Fare')
    Embarked = st.text_input('Embarked')
    result = ''

    #SESSION No. 06, 26/11/2024, 2 hours
    #This code ensures that when the button 'Predict' is clicked, the PredictionFunction
    #which is defined above is called to make the prediction and store in the variable
    #'result'

    if st.button('Predict'):
        #Convert the inputs to appropriate data types
        Pclass = int(Pclass)
        Age = float(Age)
        SibSp = int(SibSp)
        Parch = int(Parch)
        Fare = float(Fare)
        result = PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
    st.success(f'The output is: {result}')


main()


