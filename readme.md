### A Unified Interface for IQA Datasets

This repository contains a unified interface for **downloading and loading** 20 popular Image Quality Assessment (IQA) datasets. We provide codes for both general **Python** and **PyTorch**.

#### Citation

This repository is part of our [Bayesian IQA project](http://ivc.uwaterloo.ca/research/bayesianIQA/) where we present an overview of IQA methods from a Bayesian perspective. More detailed summaries of both IQA models and datasets can be found in this [interactive webpage](http://ivc.uwaterloo.ca/research/bayesianIQA/).

If you find our project useful, please cite our paper
```
@article{duanmu2021biqa,
        author = {Duanmu, Zhengfang and Liu, Wentao and Wang, Zhongling and Wang, Zhou},
        title = {Quantifying Visual Image Quality: A Bayesian View},
        journal = {Annual Review of Vision Science},
        volume = {7},
        number = {1},
        pages = {437-464},
        year = {2021}
        }
```

#### Supported Datasets

|                                        Dataset                                        |                  Dis Img                   |      Ref Img       |                                                         MOS                                                          |        DMOS        |
| :-----------------------------------------------------------------------------------: | :----------------------------------------: | :----------------: | :------------------------------------------------------------------------------------------------------------------: | :----------------: |
|          [LIVE](https://live.ece.utexas.edu/research/quality/subjective.htm)          |             :heavy_check_mark:             | :heavy_check_mark: |                                                                                                                      | :heavy_check_mark: |
|            [A57](http://vision.eng.shizuoka.ac.jp/mod/page/view.php?id=26)            |             :heavy_check_mark:             | :heavy_check_mark: |                                                                                                                      | :heavy_check_mark: |
| [LIVE_MD](https://live.ece.utexas.edu/research/Quality/live_multidistortedimage.html) |             :heavy_check_mark:             | :heavy_check_mark: |                                                                                                                      | :heavy_check_mark: |
|               [MDID2013](https://ieeexplore.ieee.org/document/6879255)                |             :heavy_check_mark:             | :heavy_check_mark: |                                                                                                                      | :heavy_check_mark: |
|           [CSIQ](http://vision.eng.shizuoka.ac.jp/mod/page/view.php?id=23)            |             :heavy_check_mark:             | :heavy_check_mark: |                                                                                                                      | :heavy_check_mark: |
|            [KADID-10k](http://database.mmsp-kn.de/kadid-10k-database.html)            |             :heavy_check_mark:             | :heavy_check_mark: | :heavy_check_mark:<sub>[(Note)](https://github.com/icbcbicc/IQA-Dataset/issues/3#issuecomment-2192649304)</sub> ~~~~ |                    |
|                  [TID2008](http://www.ponomarenko.info/tid2008.htm)                   |             :heavy_check_mark:             | :heavy_check_mark: |                                                  :heavy_check_mark:                                                  |                    |
|                  [TID2013](http://www.ponomarenko.info/tid2013.htm)                   |             :heavy_check_mark:             | :heavy_check_mark: |                                                  :heavy_check_mark:                                                  |                    |
|              [CIDIQ_MOS100](https://www.ntnu.edu/web/colourlab/software)              |             :heavy_check_mark:             | :heavy_check_mark: |                                                  :heavy_check_mark:                                                  |                    |
|              [CIDIQ_MOS50](https://www.ntnu.edu/web/colourlab/software)               |             :heavy_check_mark:             | :heavy_check_mark: |                                                  :heavy_check_mark:                                                  |                    |
|  [MDID2016](https://www.sciencedirect.com/science/article/abs/pii/S0031320316301911)  |             :heavy_check_mark:             | :heavy_check_mark: |                                                  :heavy_check_mark:                                                  |                    |
|           [SDIVL](http://www.ivl.disco.unimib.it/activities/imagequality/)            |             :heavy_check_mark:             | :heavy_check_mark: |                                                  :heavy_check_mark:                                                  |                    |
|           [MDIVL](http://www.ivl.disco.unimib.it/activities/imagequality/)            |             :heavy_check_mark:             | :heavy_check_mark: |                                                  :heavy_check_mark:                                                  |                    |
|                 [Toyama](http://mict.eng.u-toyama.ac.jp/mictdb.html)                  |             :heavy_check_mark:             | :heavy_check_mark: |                                                  :heavy_check_mark:                                                  |                    |
|            [PDAP-HDDS](https://sites.google.com/site/eelab907/zi-liao-ku)             |             :heavy_check_mark:             | :heavy_check_mark: |                                                  :heavy_check_mark:                                                  |                    |
|                 [VCLFER](https://www.vcl.fer.hr/quality/vclfer.html)                  |             :heavy_check_mark:             | :heavy_check_mark: |                                                  :heavy_check_mark:                                                  |                    |
|               [PIPAL](https://www.jasongt.com/projectpages/pipal.html)                |             :heavy_check_mark:             | :heavy_check_mark: |                                                  :heavy_check_mark:                                                  |                    |
|     [LIVE_Challenge](https://live.ece.utexas.edu/research/ChallengeDB/index.html)     |             :heavy_check_mark:             |                    |                                                  :heavy_check_mark:                                                  |                    |
|               [CID2013](https://zenodo.org/record/2647033#.YDSi73X0kUc)               |             :heavy_check_mark:             |                    |                                                  :heavy_check_mark:                                                  |                    |
|            [KonIQ-10k](http://database.mmsp-kn.de/koniq-10k-database.html)            |             :heavy_check_mark:             |                    |                                                  :heavy_check_mark:                                                  |                    |
|                        [SPAQ](https://github.com/h4nwei/SPAQ)                         |             :heavy_check_mark:             |                    |                                                  :heavy_check_mark:                                                  |                    |
|           [AADB](https://github.com/aimerykong/deepImageAestheticsAnalysis)           |             :heavy_check_mark:             |                    |                                                  :heavy_check_mark:                                                  |                    |
|                 [BIQ2021](https://github.com/nisarahmedrana/BIQ2021)                  |             :heavy_check_mark:             |                    |                                                  :heavy_check_mark:                                                  |                    |
|                 [FLIVE](https://github.com/niu-haoran/FLIVE_Database)                 |             :heavy_check_mark:             |                    |                                                  :heavy_check_mark:                                                  |                    |
|         [Waterloo_Exploration](https://ece.uwaterloo.ca/~k29ma/exploration/)          |             :heavy_check_mark:             | :heavy_check_mark: |                                                                                                                      |                    |
|      [<del>KADIS-700k</del>](http://database.mmsp-kn.de/kadid-10k-database.html)      | :heavy_check_mark:  <sub>(code only)</sub> | :heavy_check_mark: |                                                                                                                      |                    |

#### Basic Usage

0. Prerequisites
    ```shell
    pip install wget
    ```

1. General Python (please refer [```demo.py```](demo.py))

    ```python
    from load_dataset import load_dataset
    dataset = load_dataset("LIVE")
    ```

2. PyTorch (please refer [```demo_pytorch.py```](demo_pytorch.py))

    ```python
    from load_dataset import load_dataset_pytorch
    dataset = load_dataset_pytorch("LIVE")
    ```

#### Advanced Usage

1. General Python (please refer [```demo.py```](demo.py))

    ```python
    from load_dataset import load_dataset
    dataset = load_dataset("LIVE", dataset_root="data", attributes=["dis_img_path", "dis_type", "ref_img_path", "score"], download=True)
    ```

2. PyTorch (please refer [```demo_pytorch.py```](demo_pytorch.py))

    ```python
    from load_dataset import load_dataset_pytorch
    transform = transforms.Compose([transforms.RandomCrop(size=64), transforms.ToTensor()])
    dataset = load_dataset_pytorch("LIVE", dataset_root="data", attributes=["dis_img_path", "dis_type", "ref_img_path", "score"], download=True, transform=transform)
    ```

#### TODO

- [ ] [AVA](https://github.com/mtobeiyf/ava_downloader)
- [x] [PIPAL](https://www.jasongt.com/projectpages/pipal.html)
- [x] [AADB](https://github.com/aimerykong/deepImageAestheticsAnalysis)
- [x] [FLIVE](https://github.com/niu-haoran/FLIVE_Database/blob/master/database_prep.ipynb)
- [x] [BIQ2021](https://github.com/nisarahmedrana/BIQ2021)
- [ ] [IVC](http://ivc.univ-nantes.fr/en/databases/Subjective_Database/)
- [ ] PyPI package
- [ ] HuggingFace dataset
- [ ] Provide more attributes
- [ ] ~~Add TensorFlow support~~
- [ ] ~~Add MATLAB support~~

#### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=icbcbicc/IQA-Dataset&type=Date)](https://star-history.com/#icbcbicc/IQA-Dataset&Date)