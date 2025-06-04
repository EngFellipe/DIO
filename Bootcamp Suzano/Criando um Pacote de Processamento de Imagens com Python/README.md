# 📦 whatsapp_stickerizer

**Transforme qualquer imagem em uma figurinha compatível com o WhatsApp — em Python.**

![badge](https://img.shields.io/badge/license-MIT-green)
![badge](https://img.shields.io/badge/status-em%20desenvolvimento-blue)

---

## 🧠 Sobre o Projeto

O `whatsapp_stickerizer` é um pacote Python criado com o objetivo de facilitar a conversão de imagens em **figurinhas WebP compatíveis com o WhatsApp**, de forma simples, automatizada e personalizável.

Esse projeto surgiu como exercício prático para aplicar os conceitos de **modularização**, **empacotamento em Python** e publicação no **PyPI**, apresentados no conteúdo da Karina Kato: *Descomplicando a criação de pacotes Python*.

---

## ✨ Funcionalidades

- 📐 Redimensiona imagens automaticamente para 512x512 px
- 🧼 Remove fundo branco (futuro)
- 💾 Converte para o formato `.webp` com otimização
- ⚡ Uso direto via script ou importação como módulo
- 🔧 Pronto para empacotamento e publicação no PyPI

---

## 🛠️ Como usar

### Instalação local (direto do repositório)

```bash
git clone https://github.com/seuusuario/whatsapp_stickerizer.git
cd whatsapp_stickerizer
pip install .

# Uso em script Python

from whatsapp_stickerizer.converter import imagem_para_sticker

imagem_para_sticker("sua_imagem.jpg", "figurinha.webp")


💡 Etapas da Elaboração

    1. Estruturação do projeto com base no template simple-package-template

    2. Criação do módulo converter.py com Pillow

    3 .Escrita de setup.py, requirements.txt e README.md

    4. Geração da distribuição (sdist, wheel)

    5. Testes locais e validação do pacote

    6 .Preparação para publicação no Test PyPI / PyPI oficial


📁 Estrutura do Projeto

whatsapp_stickerizer/
│
├── whatsapp_stickerizer/
│   ├── __init__.py
│   └── converter.py
│
├── setup.py
├── requirements.txt
├── LICENSE
└── README.md
