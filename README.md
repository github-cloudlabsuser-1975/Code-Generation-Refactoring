# Code-Generation-Refactoring

Este proyecto contiene varios scripts de ejemplo en Python para practicar refactorización, pruebas unitarias y manejo de errores. Incluye una calculadora simple, un script para sumar elementos, un ejemplo de integración con la API de OpenWeatherMap y otros ejemplos básicos.

## Estructura del proyecto

- `calculator.py`: Calculadora simple con operaciones básicas (sumar, restar, multiplicar, dividir).
- `sum_elements.py`: Solicita al usuario una cantidad de números y calcula su suma.
- `weather_script.py`: API REST con Flask que consulta el clima de una ciudad usando OpenWeatherMap.
- `card_draw.py`: Ejemplo de sorteo de cartas (con errores intencionales para practicar depuración).
- `hello.py`: Script básico que imprime "Hello, world!".
- `test_calculator.py`: Pruebas unitarias para la calculadora usando pytest.
- `test_weather_script.py`: Pruebas unitarias para el API de clima.
- `requirements.txt`: Lista de dependencias necesarias.

## Instalación

1. Clona el repositorio.
2. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

- **Calculadora:**
  ```sh
  python calculator.py
  ```
- **Sumar elementos:**
  ```sh
  python sum_elements.py
  ```
- **API de clima:**
  1. Coloca tu API key de OpenWeatherMap en `weather_script.py`.
  2. Ejecuta:
     ```sh
     python weather_script.py
     ```
  3. Accede a `http://localhost:5000/weather?city=Ciudad` desde tu navegador o Postman.

## Pruebas

Ejecuta las pruebas unitarias con:
```sh
pytest
```

## Notas

- El archivo `card_draw.py` contiene errores intencionales para practicar depuración.
- Recuerda reemplazar `'TU_API_KEY_AQUI'` en `weather_script.py` por tu clave real de OpenWeatherMap.

---
