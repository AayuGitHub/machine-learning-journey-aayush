# dataset_class.py

class Dataset:
    def __init__(self, name, num_samples, num_features):
        """
        Dataset blueprint.
        name: string representing name of dataset (e.g. 'Iris', 'MNIST')
        num_samples: total rows / items
        num_features: number of columns/features
        """
        self.name = name
        self.num_samples = num_samples
        self.num_features = num_features

    def summary(self):
        '''
        Print dataset summary.
        ''' 
        print("===== Dataset Summary =====")
        print(f"Name: {self.name}")
        print(f"Samples: {self.num_samples}")
        print(f"Features: {self.num_features}")
        print("===========================")

if __name__ == "__main__":
    ds = Dataset("Iris", 150, 4)
    ds.summary()
