from setuptools import setup

setup(
    name="iqadataset",
    version="0.1.1",
    description="A collection of Image Quality Assessment (IQA) datasets",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    author="Zhongling Wang",
    author_email="zhongling.wang@uwaterloo.ca",
    url="https://github.com/icbcbicc/IQA-Dataset",
    packages=["iqadataset"],
    install_requires=[
        "pandas",
        "pillow",
        "torch",
        "torchvision",
        "wget"
    ],
    include_package_data=True,
    package_data={
        "iqadataset": ["iqadataset/csv/*.txt"]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Image Processing"
    ],
    python_requires=">=3.6"
)
