# TF03 - Sistema de Blog Multi-Container

## Aluno

* **Nome:** Paulo Vinicius Bernardes 
* **RA:** 6324010
* **Curso:** Análise e Desenvolvimento de Sistemas
* **Disciplina:** Implementação de Software

---

## Descrição

Este projeto implementa um sistema de blog utilizando **Docker Compose** para orquestrar múltiplos serviços.

O sistema possui:

* **Nginx** como proxy reverso
* **Frontend** para interface do usuário
* **Backend** com API REST
* **MySQL** para persistência de dados

Todos os containers se comunicam através de uma **rede Docker personalizada**.

---

## Como executar

Entrar na pasta do projeto:

```bash
cd TF03
```

Subir os containers:

```bash
docker compose up -d --build
```

Verificar se estão rodando:

```bash
docker compose ps
```

---

## Acesso

Frontend:

http://localhost

API:

http://localhost/api/posts

---


