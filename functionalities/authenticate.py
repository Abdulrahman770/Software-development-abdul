import pandas as pd


class Authenticate:
    def auth(userId):
        df = pd.read_csv("./data/users.csv")
        for i in range(len(df)):
            if(df['Id'][i]==userId):
                return [1, df['type'][i]]

        return [-1, -1]