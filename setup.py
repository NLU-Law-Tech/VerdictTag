import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()
    
with open('requirements.txt','r',encoding = 'utf-8') as f:
    requirements = f.read().split("\n")

setuptools.setup(
    name="VerdictTag", 
    version='0.0.1',
    description="tag the license, phone number and bank account in the verdict", #簡介
    long_description=long_description, #顯示於 pypi 的介紹
    long_description_content_type="text/markdown",
    url="https://github.com/NLU-Law-Tech/VerdictTag.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires = requirements
)