import pandas as pd


class IQADataset():
    def __init__(self, csv_file, name, dataset_root, attributes):

        self.df = pd.read_csv(csv_file, dtype=str)
        self.name = name
        self.dataset_root = dataset_root
        self.attributes = attributes

        self.length = len(self.df)

    def __str__(self):
        return f"IQADataset ({self.name}), attributes: {self.attributes}"

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        if idx >= self.length:
            raise StopIteration

        sample = {}
        for attr in self.attributes:
            sample[attr] = self.df[attr][idx]
            if attr == "score":
                sample[attr] = float(self.df[attr][idx])

        return sample
