# 🤖 Job Listings Scraper — El Empleo

**ES** 

---

## 📌 Descripción

Bot que automatiza la búsqueda de ofertas de trabajo en [elempleo.com](https://www.elempleo.com), extrae título, empresa, ciudad, salario y enlace de cada oferta, y exporta los resultados a un archivo Excel.

Proyecto desarrollado como parte de un plan de aprendizaje de Python enfocado en automatización de procesos.

## 🛠️ Tecnologías

- `playwright` — automatización de browser para renderizado de páginas dinámicas
- `beautifulsoup4` — parsing de HTML
- `pandas` + `openpyxl` — exportación a Excel

## 📁 Estructura

```
job-listings-scraper/
├── main.py
├── .gitignore
├── Config/
│   └── settings.py
├── Logic/
│   ├── scraper.py
│   └── exporter.py
└── Data/
    └── resultados.xlsx
```

## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/SergioArdCr/job-listings-scraper.git
cd job-listings-scraper

# Instalar dependencias
pip install playwright beautifulsoup4 pandas openpyxl

# Instalar browser de Playwright
playwright install chromium
```

## ⚙️ Configuración

En `Config/settings.py` puedes ajustar:

```python
KEYWORD = "python"       # término de búsqueda
CIUDAD  = "bogota"       # ciudad del filtro
MAX_OFERTAS = 20         # máximo de resultados a extraer
```

## 🚀 Uso

```bash
python main.py
```

El bot abre el browser, navega a El Empleo, extrae las ofertas y guarda `Data/resultados.xlsx`.

## 📊 Ejemplo de salida

![alt text](image.png)

## 🔍 Decisiones técnicas

Este proyecto presentó un reto interesante: la página usa **Handlebars del lado del servidor**, lo que significa que los datos llegan en el HTML pero dentro de atributos con JSON escapado (`&quot;`). El enfoque final combina Playwright para renderizar la página y BeautifulSoup para parsear el HTML resultante.

Proceso de debugging:
1. Inspección del DOM con DevTools
2. Intercepción de llamadas de red con `page.on("response")`
3. Lectura del HTML renderizado con `page.content()`
4. Parsing con BeautifulSoup y extracción del atributo `data-ga4-offerdata`

## 💡 Aprendizajes clave

- Diferencia entre contenido renderizado por servidor vs. JavaScript
- Uso de `page.on("response")` para interceptar llamadas de red
- Combinación de Playwright + BeautifulSoup para páginas complejas
- Debugging iterativo con `page.screenshot()` e `inner_html()`

---

---

# 🤖 Job Listings Scraper — El Empleo

**EN**

---

## 📌 Description

A bot that automates job searches on [elempleo.com](https://www.elempleo.com), extracts title, company, city, salary, and link from each listing, and exports the results to an Excel file.

Built as part of a Python learning plan focused on process automation.

## 🛠️ Tech Stack

- `playwright` — browser automation for dynamic page rendering
- `beautifulsoup4` — HTML parsing
- `pandas` + `openpyxl` — Excel export

## 📁 Structure

```
job-listings-scraper/
├── main.py
├── .gitignore
├── Config/
│   └── settings.py
├── Logic/
│   ├── scraper.py
│   └── exporter.py
└── Data/
    └── resultados.xlsx
```

## ⚙️ Setup

```bash
# Clone the repository
git clone https://github.com/SergioArdCr/job-listings-scraper.git
cd job-listings-scraper

# Install dependencies
pip install playwright beautifulsoup4 pandas openpyxl

# Install Playwright browser
playwright install chromium
```

## ⚙️ Configuration

In `Config/settings.py` you can adjust:

```python
KEYWORD     = "python"   # search term
CIUDAD      = "bogota"   # city filter
MAX_OFERTAS = 20         # maximum results to extract
```

## 🚀 Usage

```bash
python main.py
```

The bot opens the browser, navigates to El Empleo, scrapes the listings, and saves `Data/resultados.xlsx`.

## 🔍 Technical Decisions

This project presented an interesting challenge: the page uses **server-side Handlebars**, meaning data arrives in the HTML but inside attributes with escaped JSON (`&quot;`). The final approach combines Playwright to render the page and BeautifulSoup to parse the resulting HTML.

Debugging process:
1. DOM inspection with DevTools
2. Network call interception with `page.on("response")`
3. Reading rendered HTML with `page.content()`
4. BeautifulSoup parsing and `data-ga4-offerdata` attribute extraction

## 💡 Key Learnings

- Difference between server-rendered and JavaScript-rendered content
- Using `page.on("response")` to intercept network calls
- Combining Playwright + BeautifulSoup for complex pages
- Iterative debugging with `page.screenshot()` and `inner_html()`
