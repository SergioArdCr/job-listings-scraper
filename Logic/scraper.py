import json
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from Config.settings import URL_BUSQUEDA, MAX_OFERTAS

def obtener_ofertas() -> list[dict]:
    ofertas = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"Navegando a: {URL_BUSQUEDA}")
        page.goto(URL_BUSQUEDA, timeout=30000)
        page.wait_for_selector(".result-item", timeout=15000)
        page.wait_for_load_state("networkidle", timeout=15000)

        # BeautifulSoup parsea el HTML completo que Playwright tiene en memoria
        soup = BeautifulSoup(page.content(), "html.parser")
        browser.close()

    # Busca los divs que tienen data-ga4-offerdata con contenido real
    tarjetas = soup.select("div.js-area-bind[data-ga4-offerdata]")
    
    # Filtra los que tienen el atributo vacío (hay duplicados sin datos)
    tarjetas = [t for t in tarjetas if t.get("data-ga4-offerdata")]

    print(f"Ofertas encontradas: {len(tarjetas)}")

    for tarjeta in tarjetas[:MAX_OFERTAS]:
        try:
            data = json.loads(tarjeta["data-ga4-offerdata"])
            enlace = tarjeta.get("data-url", "")

            ofertas.append({
                "titulo":  data.get("title", ""),
                "empresa": data.get("company", ""),
                "ciudad":  data.get("location", ""),
                "salario": data.get("salary", ""),
                "enlace":  f"https://www.elempleo.com{enlace}"
            })
        except Exception as e:
            print(f"Error en tarjeta: {e}")
            continue

    return ofertas