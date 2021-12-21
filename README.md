# Mensageria de usuários genéricos
## Objetivo
Aplicativo desenvolvido em Python, que traz uma lista de usuários, nome e CPF, de forma genérica.
## Stack
- Docker
- Confluent Kafka
- ZooKeeper
- Kafdrop
- Python 3.9
- Gerador de Nomes de Central de Dados (https://github.com/centraldedados/gerador-nomes#api)

## Funcionamento

A aplicação é executada à partir do comando:

```
python3 producer.py
```

A mesma também está no build do Container.

A aplicação producer.py também contém o comando -c, que dita quantos usuários deve ser gerada a informação. Caso -c seja omitido, um total de 10 usuários serão gerados.

Os nomes são gerados à partir da composição dos endpoints __/nomes__ e __/apelidos/__ do Gerador de Nomes. Já para os CPFs é utilizado um algoritmo próprio realizando a validação à partir dos dígitos verificadores.

## Instalação e uso

Executar o docker-composer:

```
docker-compose docker-compose.yml -d

```

O producer também é executado no composer. O resultado da execução ficará disponível no Kafdrop na seguinte url: http://localhost:9000/ no tópico __new-customers__