from setuptools import setup, find_packages

setup(
    name="gsu_transformer_sim",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["numpy","matplotlib","networkx","streamlit"],
)
