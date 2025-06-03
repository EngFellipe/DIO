# Exemplos - Language Studio

## 1. Análise de Sentimento e opinião

**Texto:**

> "Já cliquei no botão de descadastro diversas vezes no e-mail e não paro de receber e-mails de marketing. São volumosos e não respeitam o descadastro. Não há opção no perfil de usuário para desativar."

**Resultado:**

```json
{
    "documents": [
        {
            "id": "id__1342",
            "sentiment": "negative",
            "confidenceScores": {
                "positive": 0,
                "neutral": 0.03,
                "negative": 0.97
            },
            "sentences": [
                {
                    "sentiment": "neutral",
                    "confidenceScores": {
                        "positive": 0,
                        "neutral": 0.82,
                        "negative": 0.17
                    },
                    "offset": 0,
                    "length": 104,
                    "text": "Já cliquei no botão de descadastro diversas vezes no e-mail e não paro de receber e-mails de marketing. ",
                    "targets": [],
                    "assessments": []
                },
                {
                    "sentiment": "negative",
                    "confidenceScores": {
                        "positive": 0,
                        "neutral": 0.01,
                        "negative": 0.99
                    },
                    "offset": 104,
                    "length": 45,
                    "text": "São volumosos e não respeitam o descadastro. ",
                    "targets": [],
                    "assessments": []
                },
                {
                    "sentiment": "negative",
                    "confidenceScores": {
                        "positive": 0,
                        "neutral": 0.06,
                        "negative": 0.94
                    },
                    "offset": 149,
                    "length": 49,
                    "text": "Não há opção no perfil de usuário para desativar.",
                    "targets": [],
                    "assessments": []
                }
            ],
            "warnings": []
        }
    ],
    "errors": [],
    "modelVersion": "2025-01-01"
}
```

---

