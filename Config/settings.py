import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Búsqueda
KEYWORD = "RPA"
CIUDAD = "bogota"
URL_BUSQUEDA = f"https://www.elempleo.com/co/ofertas-empleo/{CIUDAD}/trabajo-{KEYWORD}?PublishDate=hace-1-semana"
MAX_OFERTAS = 10

# Exportación
RESULTADO_PATH = os.path.join(BASE_DIR, "Data", "resultados.xlsx")