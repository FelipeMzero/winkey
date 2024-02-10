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

def set_product_key(product_key):
    try:
        key_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, "ProductKey", 0, winreg.REG_MULTI_SZ, product_key)
            print("Chave do produto definida com sucesso.")
    except Exception as e:
        print("Erro ao definir a chave do produto:", e)

def main():
    while True:
        print("Menu:")
        print("1. Obter chave do produto instalada")
        print("2. Definir chave do produto")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            installed_product_key = get_installed_product_key()
            if installed_product_key:
                formatted_key = '-'.join(installed_product_key)
                print("Chave do produto instalada:", formatted_key)
            else:
                print("Nenhuma chave do produto instalada.")
        elif choice == "2":
            product_keys = input("Insira as chaves do produto do Windows (separadas por traço): ").split('-')
            set_product_key(product_keys)
        elif choice == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
