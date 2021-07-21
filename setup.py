from setuptools import _install_setup_requires, setup
def readme():
    with open('README.md') as f:
        return f.read()


setup(name='stats265',
    version='0.75',
    description='Statistics distributions from 265',
    packages=['stats265'],
    license="MIT",
    author="Tanyaradzwa Gozhora",
    author_email="tanyaradzwagozhora@gmail.com",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/TanyaradzwaGozhora/stats265",
    download_url ="https://github.com/TanyaradzwaGozhora/stats265/releases/tag/v0.75",
    keywords = ["STATS", "STATISTICS", "DISTRIBUTION"],
    install_requires=[
        "math",
        "matplotlib"
         ],
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
