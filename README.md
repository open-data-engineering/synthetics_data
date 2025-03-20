# 📊 Módulo de Geração de Dados Sintéticos

## 🚀 Visão Geral
Este módulo tem como objetivo gerar dados sintéticos realistas utilizando a biblioteca Faker. Ele pode ser integrado facilmente a aplicações que utilizam Kafka, PubSub ou outras plataformas de mensageria para simulação de eventos em pipelines de dados.

## 📌 Funcionalidades
- 🎲 **Geração de dados aleatórios**: Simula usuários, pedidos, transações e outros eventos personalizados.
- 📦 **Formato flexível**: Retorna os dados em JSON, CSV ou outros formatos conforme necessidade.
- ⚡ **Alta performance**: Utiliza Faker para gerar dados de maneira eficiente e escalável.
- 🔌 **Fácil integração**: Pode ser utilizado em aplicações que produzem eventos para Kafka, PubSub e outras plataformas.

## 📦 Instalação
Para instalar e utilizar o módulo, siga os passos abaixo:

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/synthetic-data-generator.git
cd synthetic-data-generator

# Instale as dependências
pip install -r requirements.txt
```

## ⚙️ Uso
Exemplo de geração de um conjunto de dados sintéticos:

```python
from generator.core import SyntheticDataGenerator

generator = SyntheticDataGenerator(num_records=1000)
data = generator.generate()

print(data)  # Retorna uma lista de dicionários com os dados gerados
```

### Exemplo de Integração com Kafka
Para enviar os dados diretamente para um tópico Kafka:

```python
from generator.core import SyntheticDataGenerator
from kafka import KafkaProducer
import json

generator = SyntheticDataGenerator(num_records=100)
data = generator.generate()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for record in data:
    producer.send('synthetic-data-topic', record)
producer.flush()
```

### Exemplo de Integração com Google PubSub
```python
from generator.core import SyntheticDataGenerator
from google.cloud import pubsub_v1
import json

generator = SyntheticDataGenerator(num_records=100)
data = generator.generate()

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("meu-projeto", "synthetic-data-topic")

for record in data:
    publisher.publish(topic_path, json.dumps(record).encode("utf-8"))
```

## 📂 Estrutura do Módulo
```
synthetic-data-generator/
├── generator/
│   ├── __init__.py
│   ├── core.py  # Lógica principal de geração de dados
│   ├── schemas/  # Definições opcionais de schemas
│
├── tests/  # Testes unitários
│   ├── test_generator.py
│
├── examples/  # Exemplos de uso
│   ├── generate_kafka.py
│   ├── generate_pubsub.py
│
├── requirements.txt  # Dependências do projeto
├── README.md  # Documentação principal
```

## 🛠 Tecnologias Utilizadas
- **Python** 🐍
- **Faker** para geração de dados fictícios
- **Kafka-Python** para integração com Kafka
- **Google Cloud PubSub** para integração com PubSub

## 📌 Contribuição
Sinta-se à vontade para contribuir! Para propor melhorias:
1. Faça um fork do repositório
2. Crie uma branch para a feature/bugfix (`git checkout -b feature-nova`)
3. Commit suas alterações (`git commit -m "Adicionando nova funcionalidade"`)
4. Push para a branch (`git push origin feature-nova`)
5. Abra um Pull Request 🚀

## 📜 Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

## 📞 Contato
- 📧 Email: tiagornavarro@gmail.com
- 🐦 Twitter: [@tiagornavarro](https://x.com/)
- 💼 LinkedIn: [Tiago Navarro](https://www.linkedin.com/in/tiagornavarro/)

