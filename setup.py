from setuptools import find_packages,setup
setup(name="mcqs_generator",
      version="0.0.1",
      author="hasan",
      author_email="hasan@gmail.com",
      install_requires=["pandas",
"numpy",
"langchain",
"HuggingFace",
"streamlit",
"python-dotenv",
"pyPDF2"],packages=find_packages())# its work find the local pacakage below
# where ever the __init__.py find it will consider as a pacakage (find_pakages)