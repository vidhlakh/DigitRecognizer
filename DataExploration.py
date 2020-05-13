import pandas as pd
class DigitRecognizer():
    def data_explore(self):
        self.readRata = pd.read_csv("Dataset/sample_submission.csv")
        print(self.readData.head())