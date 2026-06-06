# Analizador Léxico (FLEX + Python)

Este repositorio contiene el código fuente y el ejecutable de un **Analizador Léxico** desarrollado mediante una arquitectura desacoplada. El proyecto sirve como la primera fase de un compilador, encargándose de leer un flujo de caracteres, agruparlos en lexemas y producir tokens categorizados.

## Arquitectura del Proyecto

El proyecto está dividido en dos componentes principales para separar la lógica de compilación de la experiencia de usuario:

* **Backend (FLEX / C):** El núcleo del analizador. Utiliza expresiones regulares definidas en FLEX para generar un Autómata Finito Determinista (AFD) en C que procesa el texto y clasifica los tokens.
* **Frontend (Python / Tkinter):** Interfaz gráfica de usuario (GUI) que captura el código fuente ingresado, invoca al backend mediante un subproceso (`subprocess`) y muestra los resultados en una tabla estructurada.

## Especificación del Lenguaje ("MiniLang")

El analizador está configurado para reconocer un subconjunto de reglas léxicas básicas similares a C/Java:

* **Palabras Reservadas:** `if`, `else`, `while`, `int`, `return`
* **Identificadores:** Cadenas que inician con una letra o guion bajo, seguidas de letras, números o guiones bajos. (Ej: `edad`, `contador_1`)
* **Números:** Valores numéricos enteros o decimales. (Ej: `25`, `3.14`)
* **Operadores:** `+`, `-`, `*`, `/`, `=`, `<`, `>`
* **Símbolos:** `{`, `}`, `(`, `)`, `;`
* **Ignorados:** Espacios en blanco, tabulaciones y saltos de línea.
* **Manejo de Errores:** Cualquier carácter no reconocido por las reglas anteriores se clasifica como `ERROR_LEXICO`.

## Requisitos del Sistema

Para ejecutar el código fuente desde cero, necesitas tener instalados en tu sistema y agregados a las variables de entorno (PATH):
* [Python 3.x](https://www.python.org/downloads/)
* Compilador C (`gcc`)
* Generador léxico (`flex`)
> **Nota para usuarios de Windows:** Se recomienda usar [MSYS2](https://www.msys2.org/) o MinGW para instalar `gcc` y `flex` fácilmente.

## Cómo Ejecutar el Proyecto

### Opción 1: Usar el ejecutable directamente (Recomendado)
Si ya tienes Python instalado, no necesitas compilar el backend.
1. Clona este repositorio o descarga el `.zip`.
2. Asegúrate de que `AnalizadorLexico.exe` e `interfaz.py` estén en la misma carpeta.
3. Abre una terminal en esa carpeta y ejecuta:
   ```bash
   python interfaz.py
