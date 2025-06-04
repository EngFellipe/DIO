from setuptools import setup, find_packages

setup(
    name="whatsapp_stickerizer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["Pillow"],
    author="Fellipe",
    author_email="seuemail@example.com",
    description="Converte imagens em figurinhas compatíveis com o WhatsApp",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seuusuario/whatsapp_stickerizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
