from setuptools import setup
def readme():
    with open('README.md') as f:
        return f.read()


setup(name='gozhora_distributions',
      version='0.4',
      description='Some Stats distributions',
      packages=['gozhora_distributions'],
      author="Tanyaradzwa Gozhora",
      author_email="tanyaradzwagozhora@gmail.com",
      long_description=readme(),
      long_description_content_type="text/markdown",
      zip_safe=False)
