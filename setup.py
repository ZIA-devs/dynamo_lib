from setuptools import setup

setup(
    name="dynamo-lib",
    version="0.1.0",
    description="Biblioteca para CRUD com dynamoDB",
    author="Pedro Paulo Carvalho Vieira",
    author_email="ppaulo030601@gmail.com",
    python_requires=">=3.9",
    packages=["dynamo_lib"],  # Altere isso se o nome do seu pacote for diferente
    include_package_data=True,
    install_requires=[],
)