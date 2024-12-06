import pickle
def load_pickle_and_return(path):
        with open(path, "rb") as file:
            data = pickle.load(file)
            print(file)
            type(data)
        return data

    
    