from .load_dataset import load_dataset

if __name__ == '__main__':

    dataset = load_dataset("LIVE", dataset_root="data", download=True)

    for i, sample in enumerate(dataset):
        print(f"(img {i+1}/{len(dataset)}) dis img path: {sample['dis_img_path']}, ref img path: {sample['ref_img_path']}, MOS/DMOS={sample['score']:.3f}")
