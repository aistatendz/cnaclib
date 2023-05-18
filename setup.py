import setuptools

setuptools.setup(
    name = 'cnaclib',
    version = '0.1.1',
    author= 'BENHAMADA Nadir',
    description='Simulateur RAC',
    packages=setuptools.find_packages(),
    install_requires=["certifi>=2023.5.7",
                      "charset-normalizer>=3.1.0",
                       "cnaclib>=0.1",
                       "idna>=3.4",
                       "numpy>=1.24.3",
                        "pandas>=2.0.1",
                        "python-dateutil>=2.8.2",
                        "pytz>=2023.3",
                        "six>=1.16.0",
                        "tzdata>=2023.3",
                        "urllib3>=2.0.2"],
    python_requires=">=3.8", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)