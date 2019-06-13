[![CircleCI](https://circleci.com/gh/b2wads/maas-plus/tree/master.svg?style=shield)](https://circleci.com/gh/b2wads/maas-plus)
[![codecov](https://codecov.io/gh/b2wads/maas-plus/branch/master/graph/badge.svg)](https://codecov.io/gh/b2wads/maas-plus)


# Math as a (µ)service - Plus (+)

Esse projeto faz parte do exercício proposto no [maas](https://github.com/b2wads/maas).
Essa é a implementação da operação de soma.


# Instalando o projeto

Entre na pasta do projeto e digite:

```
pipenv install --dev
```

# Rodando os testes

Para rodas os teses, faça:

```
pipenv run test
```

Todos os testes devem passar.


# Definição do serviço

## Soma

### Endpoints

`POST /`

### Entrada

```
{
  "left": 30,
  "right": 40
}
```


### Saída

```
{
  "result": 70
}
```

# Escrevendo o endpoint

A app que conterá o endpoint que implementa uma operação matemática está em `maas/app.py`.

Nesse arquivo podemos ter múltiplas rotas, mas nesse exercício teremos apenas uma, a rota `/` que implementará uma operação matemática, dependendo de qual grupo você está e qual operação seu grupo deve implementar.


Os testes para seu endpoint estão em `tests/test_operation_template.py`. Pode copiar esse código e salvar em um outro arquivo, por exemplo, `tests/test_operation_plus.py` para os testes da operação `+`.

# Rodando localmente

Para rodar o projeto localmente, faça:

```
pipenv run python -m maas
```

Obs: Para terminar o processo digite `^\` (`Ctrl+\`) no terminal.

## Fazendo uma requisição de exemplo

Depois que o projeto estiver rodando, podemos fazer requests HTTP em `http://localhost:8080/`. Um Exemplo:

```
curl -X POST http://localhost:8080
```
