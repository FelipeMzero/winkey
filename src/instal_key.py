import winreg

def set_product_key(product_key):
    try:
        key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, "ProductKey", 0, winreg.REG_MULTI_SZ, product_key)
            print("Chave do produto definida com sucesso.")
    except Exception as e:
        print("Erro ao definir a chave do produto:", e)

if __name__ == "__main__":
    product_keys = input("Insira as chaves do produto do Windows (separadas por traço): ").split('-')
    set_product_key(product_keys)
