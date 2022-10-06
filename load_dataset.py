import os

from dataset import IQADataset


def download_dataset(remote_tar_file, dataset_root):
    import tarfile

    import wget

    def bar_custom(current, total, width=80):
        output = f"[*] Downloading: {current / total * 100:.1f}% [{current / 10**6:.0f} MB / {total / 10**6:.0f} MB]"
        return output

    local_tar_file = os.path.join(dataset_root, os.path.basename(remote_tar_file))
    wget.download(remote_tar_file, out=local_tar_file, bar=bar_custom)
    with tarfile.open(local_tar_file) as z:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(z, dataset_root)
    print(f"\n[*] Downloading finished, deleting the .tar file.")
    os.remove(local_tar_file)


def prepare_dataset(name, dataset_root, attributes, download):

    score_synthesis_datasets = ["A57", "CIDIQ_MOS100", "CSIQ", "LIVE", "LIVE_MD", "MDID2013", "MDID2016", "SDIVL", "MDIVL", "TID2008", "TID2013", "VCLFER", "KADID-10k", "Toyama"]
    score_authentic_datasets = ["LIVE_Challenge", "CID2013", "KonIQ-10k", "SPAQ"]
    nonscore_synthesis_datasets = ["Waterloo_Exploration"]
    nonscore_authentic_datasets = []

    available_datasets = score_synthesis_datasets + score_authentic_datasets + nonscore_synthesis_datasets + nonscore_authentic_datasets

    if name in score_synthesis_datasets:
        avail_attributes = ["dis_img_path", "dis_type", "ref_img_path", "score"]
    elif name in score_authentic_datasets:
        avail_attributes = ["dis_img_path", "dis_type", "score"]
    elif name in nonscore_synthesis_datasets:
        avail_attributes = ["dis_img_path", "dis_type", "ref_img_path"]
    elif name in nonscore_authentic_datasets:
        avail_attributes = ["dis_img_path", "dis_type"]
    else:
        raise NotImplementedError(f"Dataset '{name}' is not supported. Currently supported datasets are: {available_datasets}.")

    if attributes is not None:
        assert type(attributes) == list
        for attr in attributes:
            if attr not in avail_attributes:
                raise KeyError(f"[!] Attribute: {attr} is not available in {name}.")
    else:
        attributes = avail_attributes

    if not os.path.exists(dataset_root):
        os.makedirs(dataset_root)

    dataset_dir = os.path.join(dataset_root, name)
    if not os.path.exists(dataset_dir):
        if download is True:
            remote_tar_file = f"http://ivc.uwaterloo.ca/database/IQADataset/{name}.tar"
            print(f"[*] Cannnot find dataset '{name}'' in '{dataset_dir}', downloading it from '{remote_tar_file}'")
            download_dataset(remote_tar_file, dataset_root)
        else:
            raise FileNotFoundError(f"[!] Cannnot find dataset '{name}' in '{dataset_dir}', try setting 'download=True' or download it manually.")

    return attributes


def load_dataset(name, dataset_root="data", attributes=None, download=True):
    csv_file = os.path.join("csv", name) + ".txt"
    attributes = prepare_dataset(name, dataset_root, attributes, download)

    return IQADataset(csv_file, name, dataset_root, attributes)


def load_dataset_pytorch(name, dataset_root="data", attributes=None, download=True, transform=None):
    from torchvision import transforms

    from dataset_pytorch import IQADatasetPyTorch

    if transform is None:
        transform = transforms.ToTensor()
    csv_file = os.path.join("csv", name) + ".txt"
    attributes = prepare_dataset(name, dataset_root, attributes, download)

    return IQADatasetPyTorch(csv_file, name, dataset_root, attributes, transform)
