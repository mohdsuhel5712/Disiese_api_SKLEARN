# usinng pickle
import pickle
model = pickle.load(open('model.pkl','rb'))
# make function
def predict_disease(fever,cough,headche,fatigue):
      prediction = model.predict([[fever,cough,headche,fatigue]])
      return prediction[0]