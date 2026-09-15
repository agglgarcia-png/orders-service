# Orders Service

![Python](https://img.shields.io/badge/Python-3.12stAPI](https://img.shields.io/badge/FastAPI-0.
![PostgreSQL](https://img.shields.io/badge/Postgretps://img.shields.io/badge/Docker-Enabled-2496ED
![Architecture](httpso/badge/Architecture-Hexagonal-orange
![Coverage](httpsds.io/badge/Coverage-86%25-brightgreen
![Tests](https://img.shields.io/bs-33_Passed-success
https://img.shields.io/badge/Ruff-Passing-success
https://img.shields.io/badge/MyPy-Passing-success
![Security](https:/.io/badge/Security-No_Known_Vulnerabilities-success

[![CI Pipeline](https://github.com/agglgarcia-png/orders-service/actions/workflows/ci.yml/badge.svg)](https://github.com/agglgarcia-png/orders-service/actions)

API REST desarrollada con FastAPI utilizando Arquitectura Hexagonal (Clean Architecture) para la gestión de órdenes.

## Objetivo

El proyecto implementa un servicio de órdenes siguiendo principios de diseño limpio, separación de responsabilidades y buenas prácticas de desarrollo backend.
# Orders Service

API REST desarrollada con FastAPI utilizando Arquitectura Hexagonal (Clean Architecture) para la gestión de órdenes.

## Objetivo

El proyecto implementa un servicio de órdenes siguiendo principios de diseño limpio, separación de responsabilidades y buenas prácticas de desarrollo backend.

## Características

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker
- GitHub Actions
- Arquitectura Hexagonal
- Unit Testing
- Integration Testing
- Ruff
- MyPy
- Cobertura superior al 80%

---

# Arquitectura

El proyecto sigue Arquitectura Hexagonal (Ports and Adapters).

## Capas

### API

Responsable de exponer los endpoints REST mediante FastAPI.

### Application

Contiene los casos de uso del sistema.

### Domain

Contiene las entidades, reglas de negocio, excepciones y contratos.

### Infrastructure

Implementa los repositorios y el acceso a PostgreSQL.

## Estructura del proyecto

```text
app/
├── api/
│   ├── dependencies.py
│   ├── routers/
│   └── schemas/
│
├── application/
│   └── use_cases/
│
├── domain/
│   ├── entities/
│   ├── exceptions/
│   ├── repositories/
│   └── value_objects/
│
├── infrastructure/
│   ├── database/
│   └── repositories/
│
└── main.py

tests/
├── unit/
└── integration/

alembic/
```

---

# Tecnologías

| Tecnología | Uso |
|------------|-----|
| Python 3.12 | Lenguaje principal |
| FastAPI | 