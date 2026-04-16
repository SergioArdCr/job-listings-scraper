from Logic.scraper import obtener_ofertas
from Logic.exporter import exportar_excel
 
if __name__ == "__main__":
    print("\n---> Iniciando scraping")
    ofertas = obtener_ofertas()
    exportar_excel(ofertas)
    print("---> Proceso finalizado\n")