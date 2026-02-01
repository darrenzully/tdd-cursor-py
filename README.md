# tdd-cursor-python

Este proyecto se usa para demostrar TDD guiado por tests
utilizando Cursor IDE como pair programmer.

Reglas:
- Tests primero
- Código mínimo
- Refactor con seguridad

## Estructura

```
tdd-cursor-python/
├── src/
│   └── domain/
│       ├── __init__.py
│       └── permissions.py
├── tests/
│   ├── __init__.py
│   └── test_permissions.py
├── cursor_rules.md
├── pyproject.toml
└── README.md
```

## Requisitos

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) para gestión de dependencias

## Uso

```bash
# Sincronizar dependencias
uv sync

# Ejecutar tests
uv run pytest

# Ejecutar con cobertura (añadir pytest-cov si lo necesitas)
uv run pytest -v
```

## Reglas

Consulta `cursor_rules.md` para las convenciones de TDD y uso de Cursor en este proyecto.
