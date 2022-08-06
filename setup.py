import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topic_detector",
    version="1.0.0",
    author="Konstantin Ivanov",
    author_email="ivkest@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://kestkest.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite='pytest',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=[
        'sanic==20.12.7',
        'pytest==5.2.2',
        'pytest-sanic==1.1.2',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'run_sanic=topic_detector.server:main'
        ]
    },
    include_package_data=True
)