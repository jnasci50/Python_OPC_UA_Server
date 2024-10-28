from joblib import dump, load

# Carregar o modelo salvo
def load_model():
    model_RF = load('Machine_Model/model_random_forest.joblib')
    return  model_RF

# Função para fazer previsões
def predictive_data(data,model):
    previsoes = model.predict(data)
    return previsoes


