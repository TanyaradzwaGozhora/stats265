from setuptools import setup
def readme():
    with open('README.md') as f:
        return f.read()


setup(name='stats265',
    version='0.6',
    description='Statistics distributions from 265',
    packages=['stats265'],
    author="Tanyaradzwa Gozhora",
    author_email="tanyaradzwagozhora@gmail.com",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/TanyaradzwaGozhora/stats265",
    project_urls={
    "Stats265-distributions": "https://github.com/TanyaradzwaGozhora/stats265",
    },
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    zip_safe=False)
