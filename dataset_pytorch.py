import os

import pandas as pd
from PIL import Image
from torch.utils.data import Dataset


class IQADatasetPyTorch(Dataset):
    def __init__(self, csv_file, name, dataset_root, attributes, transform):

        self.df = pd.read_csv(csv_file, dtype=str)
        self.name = name
        self.dataset_root = dataset_root
        self.attributes = attributes
        self.transform = transform

        self.length = len(self.df)

    def __str__(self):
        return f"IQADataset ({self.name}), attributes: {self.attributes}"

    def __len__(self):
        return self.length

    def __getitem__(self, idx):

        sample = {}
        for attr in self.attributes:
            sample[attr] = self.df[attr][idx]
            if attr == "dis_img_path":
                sample["dis_img"] = self.transform(Image.open(os.path.join(self.dataset_root, self.df[attr][idx])).convert("RGB"))
            elif attr == "ref_img_path":
                sample["ref_img"] = self.transform(Image.open(os.path.join(self.dataset_root, self.df[attr][idx])).convert("RGB"))
            elif attr == "score":
                sample[attr] = float(self.df[attr][idx])
            else:
                pass

        return sample
