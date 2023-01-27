import pickle
import pandas as pd

model = pickle.load(open('my_pipe_vot.pkl', 'rb'))


cols = ['state', 'bankstate', 'naics', 'term', 'noemp', 'newexist', 'createjob',
       'retainedjob', 'franchisecode', 'urbanrural', 'revlinecr', 'lowdoc', 'grappv']

# value = [18, 'female', 4, 'no', 'northeast', 'obesity']


def predict(list_values=None):
    to_predict = dict(zip(cols, list_values))
    to_predict = pd.DataFrame(to_predict, index=[0])
    return model.predict(to_predict)[0]