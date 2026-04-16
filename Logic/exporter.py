import pandas as pd
from Config.settings import RESULTADO_PATH

def exportar_excel(ofertas: list[dict]) -> None:
    if not ofertas:
        print("No hay ofertas para exportar.")
        return

    df = pd.DataFrame(ofertas)
    df.to_excel(RESULTADO_PATH, index=False)
    print(f"Exportado: {RESULTADO_PATH} ({len(ofertas)} ofertas)")