import winreg

def get_installed_product_key():
    try:
        key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ) as key:
            product_key, _ = winreg.QueryValueEx(key, "ProductKey")
            return product_key
    except Exception as e:
        print("Erro ao obter a chave do produto:", e)
        return None

if __name__ == "__main__":
    installed_product_key = get_installed_product_key()
    if installed_product_key:
        formatted_key = '-'.join(installed_product_key)
        print("Chave do produto instalada:", formatted_key)
    else:
        print("Nenhuma chave do produto instalada.")
