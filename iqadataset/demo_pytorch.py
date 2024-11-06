from torch.utils.data import DataLoader
from torchvision import transforms

from .load_dataset import load_dataset_pytorch

if __name__ == '__main__':

    transform = transforms.Compose([transforms.RandomCrop(size=64), transforms.ToTensor()])
    dataset = load_dataset_pytorch("LIVE", dataset_root="data", download=True, transform=transform)
    dataloader = DataLoader(dataset, batch_size=10, shuffle=False)

    for i, sample in enumerate(dataloader):
        print(f"(batch {i+1}/{len(dataloader)}), shape(dis img)={sample['dis_img'].shape}")
