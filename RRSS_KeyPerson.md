# Análisis de Red Social con Grafos: Identificando Puntos Clave de Negocio 📈📊

Este proyecto demuestra cómo utilizar la teoría de grafos para modelar y analizar una red social profesional con el objetivo de identificar individuos estratégicamente posicionados que pueden servir como "puentes" clave para acceder a contactos de alto nivel, como dueños de empresas.

## 📚 Conceptos Fundamentales de Grafos Aplicados a Redes Sociales

Un **grafo** es una estructura matemática utilizada para modelar relaciones entre objetos. Consiste en:

* **Nodos (Vertices)** 🤔👥: Los "puntos" en el grafo. En una red social, cada persona es un nodo.
* **Aristas (Bordes)** 🧵🔗: Las "líneas" que conectan los nodos. En una red social, una arista representa una relación o conexión entre dos personas.
* **Pesos en las Aristas** 💪: Un valor numérico asignado a cada arista para representar la "fuerza", importancia o intensidad de la conexión. Un peso mayor indica una conexión más fuerte.
* **Centralidad** 🎯: Métricas que cuantifican la "importancia" o influencia de un nodo dentro del grafo basándose en su posición y conexiones.
    * **Centralidad de Grado Ponderado**: La suma de los pesos de todas las aristas conectadas a un nodo. Mide cuánta "fuerza" de conexión total tiene un individuo.
    * **Centralidad de Autovector (Eigenvector Centrality)** 🌟: Mide la influencia de un nodo considerando no solo cuántas conexiones tiene, sino también cuán influyentes son las personas a las que está conectado. Una conexión con una persona muy influyente contribuye más a tu centralidad de autovector que muchas conexiones con personas poco influyentes. Cuando es ponderada, también considera la fuerza (peso) de estas conexiones.

## 📝 Planteamiento del Problema: Mapeando una Red de Negocios Específica para Encontrar el Puente Clave 🌉💼

Estamos analizando una red profesional compuesta por miembros de tres empresas: "Innovate Solutions" (💡), "Creative Minds" (🎨), y "Dynamic Ventures" (📈). El objetivo es mapear las relaciones existentes y su fuerza para identificar a la persona mejor posicionada para servir como un punto de contacto estratégico para acceder a los dueños de estas empresas para oportunidades de ventas. Un factor crucial en este escenario es que **los dueños de las diferentes empresas no tienen conexiones directas entre sí**.

Los individuos en la red y sus roles son:

* **Innovate Solutions (💡):** Ana García (Dueño 👑💼), Roberto Pérez (Gerente 💪👔), Laura Torres (Empleado Senior 🧑‍💻📄), Miguel Sánchez (Empleado Junior 🧑‍💻📄).
* **Creative Minds (🎨):** Carlos López (Dueño 👑💼), Sofía Rodríguez (Gerente 💪👔), Diego Herrera (Empleado Senior 🧑‍💻📄), Elena Castro (Empleado Junior 🧑‍💻📄).
* **Dynamic Ventures (📈):** Javier Rivas (Dueño 👑💼), Patricia Soto (Gerente 💪👔), **Fernando Vargas (Empleado Senior 🧑‍💻📄)**, Isabel Flores (Empleado Junior 🧑‍💻📄).

Las relaciones profesionales entre estas personas se describen a continuación, con una "fuerza" asignada en una escala del 1 (débil) al 5 (muy fuerte). Esta estructura de conexiones ha sido diseñada específicamente para este ejercicio para destacar un punto clave:

**Relaciones Definidas en la Red:**

* **Dentro de "Innovate Solutions" (💡):**
    * Ana García 🔗 Roberto Pérez (fuerza 4)
    * Ana García 🔗 Laura Torres (fuerza 3)
    * Roberto Pérez 🔗 Laura Torres (fuerza 5)
    * Roberto Pérez 🔗 Miguel Sánchez (fuerza 4)
    * Laura Torres 🔗 Miguel Sánchez (fuerza 3)

* **Dentro de "Creative Minds" (🎨):**
    * Carlos López 🔗 Sofía Rodríguez (fuerza 5)
    * Carlos López 🔗 Diego Herrera (fuerza 4)
    * Sofía Rodríguez 🔗 Diego Herrera (fuerza 4)
    * Sofía Rodríguez 🔗 Elena Castro (fuerza 3)
    * Diego Herrera 🔗 Elena Castro (fuerza 2)

* **Dentro de "Dynamic Ventures" (📈):**
    * Javier Rivas 🔗 Patricia Soto (fuerza 5)
    * Javier Rivas 🔗 Fernando Vargas (fuerza 4)
    * Patricia Soto 🔗 Fernando Vargas (fuerza 4)
    * Patricia Soto 🔗 Isabel Flores (fuerza 3)
    * Fernando Vargas 🔗 Isabel Flores (fuerza 3)

* **Conexiones Estratégicas Clave (Inter-empresas):**
    * **Fernando Vargas** (Empleado Senior 📈) 🔗 **Ana García** (Dueña 💡) (fuerza **5**)
    * **Fernando Vargas** (Empleado Senior 📈) 🔗 **Carlos López** (Dueño 🎨) (fuerza **5**)
    * **Fernando Vargas** (Empleado Senior 📈) 🔗 **Sofía Rodríguez** (Gerente 🎨) (fuerza **4**)

* **Otras Conexiones Inter-empresas:**
    * Roberto Pérez (Gerente 💡) 🔗 Sofía Rodríguez (Gerente 🎨) (fuerza 2)
    * Laura Torres (Empleado Senior 💡) 🔗 Diego Herrera (Empleado Senior 🎨) (fuerza 3)
    * Miguel Sánchez (Empleado Junior 💡) 🔗 Elena Castro (Empleado Junior 🎨) (fuerza 2)
    * Laura Torres (Empleado Senior 💡) 🔗 Fernando Vargas (Empleado Senior 📈) (fuerza 3)
    * Diego Herrera (Empleado Senior 🎨) 🔗 Fernando Vargas (Empleado Senior 📈) (fuerza 3)
    * Elena Castro (Empleado Junior 🎨) 🔗 Fernando Vargas (Empleado Senior 📈) (fuerza 2)

**Constraint:** Los dueños (Ana García, Carlos López, Javier Rivas) **NO tienen conexiones directas** entre ellos. 🚫🤝👑

**El Desafío:**

El desafío es utilizar el análisis de grafos, específicamente la Centralidad de Autovector Ponderada, para procesar esta red definida y determinar quién, según la estructura de conexiones y su fuerza, es el individuo más influyente y, por lo tanto, el mejor "puente" para acceder a los dueños de las diferentes empresas en este escenario particular.

## ✍️ Ejercicio Sugerido: ¡Dibuja la Red Primero!

Antes de pasar al código, te invito a tomar un papel y lápiz (o una herramienta de dibujo digital) y dibujar esta red basándote en la descripción anterior. Usa diferentes formas o colores para los roles y anota la fuerza (peso) en cada línea. Visualizar la red manualmente te ayudará a entender mejor su estructura y por qué ciertas personas podrían ser más centrales. ✏️🖼️

## ✅ Resolución en Python: Construyendo, Visualizando y Analizando el Grafo 🐍📊

Utilizaremos la librería `networkx` para trabajar con el grafo y `matplotlib` para visualizarlo.

### 🛠️ Instalación

Asegúrate de tener Python instalado y luego instala las librerías necesarias:

```bash
pip install networkx matplotlib
