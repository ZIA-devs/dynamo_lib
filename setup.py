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
    install_requires=[
        "annotated-types==0.7.0",
        "boto3==1.38.28",
        "botocore==1.38.28",
        "colorama==0.4.6",
        "jmespath==1.0.1",
        "loguru==0.7.3",
        "mypy-boto3-dynamodb==1.38.4",
        "pydantic==2.11.5",
        "pydantic_core==2.33.2",
        "python-dateutil==2.9.0.post0",
        "pytz==2025.2",
        "s3transfer==0.13.0",
        "six==1.17.0",
        "typing-inspection==0.4.1",
        "typing_extensions==4.14.0",
        "urllib3==2.4.0",
    ],
)