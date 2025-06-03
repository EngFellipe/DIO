# Exemplos - Speech Studio

## 1. Reconhecimento de Fala (Speech-to-Text)

- Idiomas testados:
  - Português (Brasil) com sotaque sudeste e nordeste
- Observações:
  - Alta precisão em ambientes silenciosos
  - Erros aumentam com ruídos de fundo e sotaques mais carregados
  - Tempo de resposta rápido (quase em tempo real)

**Áudio utilizado:** `AUD-20240404-WA0000.opus`

**Frase:**

> "Você quer esperar até meio-dia para me dar uma resposta? Porque você me dando a resposta, eu faço a carta e eu te mando. Daí a gente já começa todo o trâmite de contratação."

**Resultado do reconhecimento:**

```json
[
    {
        "Id": "1e291280cfe2445693a82c9ebb3c5864",
        "RecognitionStatus": "Success",
        "Offset": 5500000,
        "Duration": 96400000,
        "Channel": 0,
        "DisplayText": "Você quer esperar até meio-dia para me dar uma resposta? Porque você me dando a resposta, eu faço a carta e eu te mando. Daí a gente já começa todo o trâmite de contratação.",
        "NBest": [
            {
                "Confidence": 0.8638898,
                "Lexical": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "ITN": "você quer esperar até meio-dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "MaskedITN": "você quer esperar até meio-dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "Display": "Você quer esperar até meio-dia para me dar uma resposta? Porque você me dando a resposta, eu faço a carta e eu te mando. Daí a gente já começa todo o trâmite de contratação.",
                "Words": [
                    {
                        "Word": "você",
                        "Offset": 5500000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "quer",
                        "Offset": 7500000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "esperar",
                        "Offset": 9100000,
                        "Duration": 3200000
                    },
                    {
                        "Word": "até",
                        "Offset": 12300000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "meio",
                        "Offset": 13500000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "dia",
                        "Offset": 16300000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "para",
                        "Offset": 19100000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "me",
                        "Offset": 20700000,
                        "Duration": 800000
                    },
                    {
                        "Word": "dar",
                        "Offset": 21500000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "uma",
                        "Offset": 22700000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "resposta",
                        "Offset": 23900000,
                        "Duration": 6800000
                    },
                    {
                        "Word": "porque",
                        "Offset": 32300000,
                        "Duration": 2400000
                    },
                    {
                        "Word": "você",
                        "Offset": 34700000,
                        "Duration": 2400000
                    },
                    {
                        "Word": "me",
                        "Offset": 37100000,
                        "Duration": 800000
                    },
                    {
                        "Word": "dando",
                        "Offset": 37900000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "a",
                        "Offset": 39900000,
                        "Duration": 400000
                    },
                    {
                        "Word": "resposta",
                        "Offset": 40300000,
                        "Duration": 8400000
                    },
                    {
                        "Word": "eu",
                        "Offset": 48700000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "faço",
                        "Offset": 50700000,
                        "Duration": 3600000
                    },
                    {
                        "Word": "a",
                        "Offset": 54300000,
                        "Duration": 400000
                    },
                    {
                        "Word": "carta",
                        "Offset": 54700000,
                        "Duration": 8400000
                    },
                    {
                        "Word": "e",
                        "Offset": 65900000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "eu",
                        "Offset": 67900000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "te",
                        "Offset": 69100000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "mando",
                        "Offset": 70700000,
                        "Duration": 4800000
                    },
                    {
                        "Word": "daí",
                        "Offset": 75500000,
                        "Duration": 3600000
                    },
                    {
                        "Word": "a",
                        "Offset": 79100000,
                        "Duration": 400000
                    },
                    {
                        "Word": "gente",
                        "Offset": 79500000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "já",
                        "Offset": 82300000,
                        "Duration": 800000
                    },
                    {
                        "Word": "começa",
                        "Offset": 83100000,
                        "Duration": 4000000
                    },
                    {
                        "Word": "todo",
                        "Offset": 87100000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "o",
                        "Offset": 89100000,
                        "Duration": 400000
                    },
                    {
                        "Word": "trâmite",
                        "Offset": 89500000,
                        "Duration": 4000000
                    },
                    {
                        "Word": "de",
                        "Offset": 93500000,
                        "Duration": 800000
                    },
                    {
                        "Word": "contratação",
                        "Offset": 94300000,
                        "Duration": 7600000
                    }
                ]
            },
            {
                "Confidence": 0.8638898,
                "Lexical": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "ITN": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "MaskedITN": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "Display": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "Words": [
                    {
                        "Word": "você",
                        "Offset": 5500000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "quer",
                        "Offset": 7500000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "esperar",
                        "Offset": 9100000,
                        "Duration": 3200000
                    },
                    {
                        "Word": "até",
                        "Offset": 12300000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "meio",
                        "Offset": 13500000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "dia",
                        "Offset": 16300000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "para",
                        "Offset": 19100000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "me",
                        "Offset": 20700000,
                        "Duration": 800000
                    },
                    {
                        "Word": "dar",
                        "Offset": 21500000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "uma",
                        "Offset": 22700000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "resposta",
                        "Offset": 23900000,
                        "Duration": 6800000
                    },
                    {
                        "Word": "porque",
                        "Offset": 32300000,
                        "Duration": 2400000
                    },
                    {
                        "Word": "você",
                        "Offset": 34700000,
                        "Duration": 2400000
                    },
                    {
                        "Word": "me",
                        "Offset": 37100000,
                        "Duration": 800000
                    },
                    {
                        "Word": "dando",
                        "Offset": 37900000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "a",
                        "Offset": 39900000,
                        "Duration": 400000
                    },
                    {
                        "Word": "resposta",
                        "Offset": 40300000,
                        "Duration": 8400000
                    },
                    {
                        "Word": "eu",
                        "Offset": 48700000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "faço",
                        "Offset": 50700000,
                        "Duration": 3600000
                    },
                    {
                        "Word": "a",
                        "Offset": 54300000,
                        "Duration": 400000
                    },
                    {
                        "Word": "carta",
                        "Offset": 54700000,
                        "Duration": 8400000
                    },
                    {
                        "Word": "e",
                        "Offset": 65900000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "eu",
                        "Offset": 67900000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "te",
                        "Offset": 69100000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "mando",
                        "Offset": 70700000,
                        "Duration": 4800000
                    },
                    {
                        "Word": "daí",
                        "Offset": 75500000,
                        "Duration": 3600000
                    },
                    {
                        "Word": "a",
                        "Offset": 79100000,
                        "Duration": 400000
                    },
                    {
                        "Word": "gente",
                        "Offset": 79500000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "já",
                        "Offset": 82300000,
                        "Duration": 800000
                    },
                    {
                        "Word": "começa",
                        "Offset": 83100000,
                        "Duration": 4000000
                    },
                    {
                        "Word": "todo",
                        "Offset": 87100000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "o",
                        "Offset": 89100000,
                        "Duration": 400000
                    },
                    {
                        "Word": "trâmite",
                        "Offset": 89500000,
                        "Duration": 4000000
                    },
                    {
                        "Word": "de",
                        "Offset": 93500000,
                        "Duration": 800000
                    },
                    {
                        "Word": "contratação",
                        "Offset": 94300000,
                        "Duration": 7600000
                    }
                ]
            },
            {
                "Confidence": 0.8638898,
                "Lexical": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "ITN": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "MaskedITN": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "Display": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "Words": [
                    {
                        "Word": "você",
                        "Offset": 5500000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "quer",
                        "Offset": 7500000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "esperar",
                        "Offset": 9100000,
                        "Duration": 3200000
                    },
                    {
                        "Word": "até",
                        "Offset": 12300000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "meio",
                        "Offset": 13500000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "dia",
                        "Offset": 16300000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "para",
                        "Offset": 19100000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "me",
                        "Offset": 20700000,
                        "Duration": 800000
                    },
                    {
                        "Word": "dar",
                        "Offset": 21500000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "uma",
                        "Offset": 22700000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "resposta",
                        "Offset": 23900000,
                        "Duration": 6800000
                    },
                    {
                        "Word": "porque",
                        "Offset": 32300000,
                        "Duration": 2400000
                    },
                    {
                        "Word": "você",
                        "Offset": 34700000,
                        "Duration": 2400000
                    },
                    {
                        "Word": "me",
                        "Offset": 37100000,
                        "Duration": 800000
                    },
                    {
                        "Word": "dando",
                        "Offset": 37900000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "a",
                        "Offset": 39900000,
                        "Duration": 400000
                    },
                    {
                        "Word": "resposta",
                        "Offset": 40300000,
                        "Duration": 8400000
                    },
                    {
                        "Word": "eu",
                        "Offset": 48700000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "faço",
                        "Offset": 50700000,
                        "Duration": 3600000
                    },
                    {
                        "Word": "a",
                        "Offset": 54300000,
                        "Duration": 400000
                    },
                    {
                        "Word": "carta",
                        "Offset": 54700000,
                        "Duration": 8400000
                    },
                    {
                        "Word": "e",
                        "Offset": 65900000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "eu",
                        "Offset": 67900000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "te",
                        "Offset": 69100000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "mando",
                        "Offset": 70700000,
                        "Duration": 4800000
                    },
                    {
                        "Word": "daí",
                        "Offset": 75500000,
                        "Duration": 3600000
                    },
                    {
                        "Word": "a",
                        "Offset": 79100000,
                        "Duration": 400000
                    },
                    {
                        "Word": "gente",
                        "Offset": 79500000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "já",
                        "Offset": 82300000,
                        "Duration": 800000
                    },
                    {
                        "Word": "começa",
                        "Offset": 83100000,
                        "Duration": 4000000
                    },
                    {
                        "Word": "todo",
                        "Offset": 87100000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "o",
                        "Offset": 89100000,
                        "Duration": 400000
                    },
                    {
                        "Word": "trâmite",
                        "Offset": 89500000,
                        "Duration": 4000000
                    },
                    {
                        "Word": "de",
                        "Offset": 93500000,
                        "Duration": 800000
                    },
                    {
                        "Word": "contratação",
                        "Offset": 94300000,
                        "Duration": 7600000
                    }
                ]
            },
            {
                "Confidence": 0.8638898,
                "Lexical": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "ITN": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "MaskedITN": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "Display": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "Words": [
                    {
                        "Word": "você",
                        "Offset": 5500000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "quer",
                        "Offset": 7500000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "esperar",
                        "Offset": 9100000,
                        "Duration": 3200000
                    },
                    {
                        "Word": "até",
                        "Offset": 12300000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "meio",
                        "Offset": 13500000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "dia",
                        "Offset": 16300000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "para",
                        "Offset": 19100000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "me",
                        "Offset": 20700000,
                        "Duration": 800000
                    },
                    {
                        "Word": "dar",
                        "Offset": 21500000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "uma",
                        "Offset": 22700000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "resposta",
                        "Offset": 23900000,
                        "Duration": 6800000
                    },
                    {
                        "Word": "porque",
                        "Offset": 32300000,
                        "Duration": 2400000
                    },
                    {
                        "Word": "você",
                        "Offset": 34700000,
                        "Duration": 2400000
                    },
                    {
                        "Word": "me",
                        "Offset": 37100000,
                        "Duration": 800000
                    },
                    {
                        "Word": "dando",
                        "Offset": 37900000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "a",
                        "Offset": 39900000,
                        "Duration": 400000
                    },
                    {
                        "Word": "resposta",
                        "Offset": 40300000,
                        "Duration": 8400000
                    },
                    {
                        "Word": "eu",
                        "Offset": 48700000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "faço",
                        "Offset": 50700000,
                        "Duration": 3600000
                    },
                    {
                        "Word": "a",
                        "Offset": 54300000,
                        "Duration": 400000
                    },
                    {
                        "Word": "carta",
                        "Offset": 54700000,
                        "Duration": 8400000
                    },
                    {
                        "Word": "e",
                        "Offset": 65900000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "eu",
                        "Offset": 67900000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "te",
                        "Offset": 69100000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "mando",
                        "Offset": 70700000,
                        "Duration": 4800000
                    },
                    {
                        "Word": "daí",
                        "Offset": 75500000,
                        "Duration": 3600000
                    },
                    {
                        "Word": "a",
                        "Offset": 79100000,
                        "Duration": 400000
                    },
                    {
                        "Word": "gente",
                        "Offset": 79500000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "já",
                        "Offset": 82300000,
                        "Duration": 800000
                    },
                    {
                        "Word": "começa",
                        "Offset": 83100000,
                        "Duration": 4000000
                    },
                    {
                        "Word": "todo",
                        "Offset": 87100000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "o",
                        "Offset": 89100000,
                        "Duration": 400000
                    },
                    {
                        "Word": "trâmite",
                        "Offset": 89500000,
                        "Duration": 4000000
                    },
                    {
                        "Word": "de",
                        "Offset": 93500000,
                        "Duration": 800000
                    },
                    {
                        "Word": "contratação",
                        "Offset": 94300000,
                        "Duration": 7600000
                    }
                ]
            },
            {
                "Confidence": 0.8638898,
                "Lexical": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "ITN": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "MaskedITN": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "Display": "você quer esperar até meio dia para me dar uma resposta porque você me dando a resposta eu faço a carta e eu te mando daí a gente já começa todo o trâmite de contratação",
                "Words": [
                    {
                        "Word": "você",
                        "Offset": 5500000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "quer",
                        "Offset": 7500000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "esperar",
                        "Offset": 9100000,
                        "Duration": 3200000
                    },
                    {
                        "Word": "até",
                        "Offset": 12300000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "meio",
                        "Offset": 13500000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "dia",
                        "Offset": 16300000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "para",
                        "Offset": 19100000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "me",
                        "Offset": 20700000,
                        "Duration": 800000
                    },
                    {
                        "Word": "dar",
                        "Offset": 21500000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "uma",
                        "Offset": 22700000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "resposta",
                        "Offset": 23900000,
                        "Duration": 6800000
                    },
                    {
                        "Word": "porque",
                        "Offset": 32300000,
                        "Duration": 2400000
                    },
                    {
                        "Word": "você",
                        "Offset": 34700000,
                        "Duration": 2400000
                    },
                    {
                        "Word": "me",
                        "Offset": 37100000,
                        "Duration": 800000
                    },
                    {
                        "Word": "dando",
                        "Offset": 37900000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "a",
                        "Offset": 39900000,
                        "Duration": 400000
                    },
                    {
                        "Word": "resposta",
                        "Offset": 40300000,
                        "Duration": 8400000
                    },
                    {
                        "Word": "eu",
                        "Offset": 48700000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "faço",
                        "Offset": 50700000,
                        "Duration": 3600000
                    },
                    {
                        "Word": "a",
                        "Offset": 54300000,
                        "Duration": 400000
                    },
                    {
                        "Word": "carta",
                        "Offset": 54700000,
                        "Duration": 8400000
                    },
                    {
                        "Word": "e",
                        "Offset": 65900000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "eu",
                        "Offset": 67900000,
                        "Duration": 1200000
                    },
                    {
                        "Word": "te",
                        "Offset": 69100000,
                        "Duration": 1600000
                    },
                    {
                        "Word": "mando",
                        "Offset": 70700000,
                        "Duration": 4800000
                    },
                    {
                        "Word": "daí",
                        "Offset": 75500000,
                        "Duration": 3600000
                    },
                    {
                        "Word": "a",
                        "Offset": 79100000,
                        "Duration": 400000
                    },
                    {
                        "Word": "gente",
                        "Offset": 79500000,
                        "Duration": 2800000
                    },
                    {
                        "Word": "já",
                        "Offset": 82300000,
                        "Duration": 800000
                    },
                    {
                        "Word": "começa",
                        "Offset": 83100000,
                        "Duration": 4000000
                    },
                    {
                        "Word": "todo",
                        "Offset": 87100000,
                        "Duration": 2000000
                    },
                    {
                        "Word": "o",
                        "Offset": 89100000,
                        "Duration": 400000
                    },
                    {
                        "Word": "trâmite",
                        "Offset": 89500000,
                        "Duration": 4000000
                    },
                    {
                        "Word": "de",
                        "Offset": 93500000,
                        "Duration": 800000
                    },
                    {
                        "Word": "contratação",
                        "Offset": 94300000,
                        "Duration": 7600000
                    }
                ]
            }
        ]
    }
]
```

---
