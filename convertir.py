import json
import yaml

def main():
    # 1. Leer datos.json
    with open('datos.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. Agregar el puerto 4
    if 'puertos' in data and isinstance(data['puertos'], list):
        if 4 not in data['puertos']:
            data['puertos'].append(4)

    # 3. Guardar como datos_modificado.json
    with open('datos_modificado.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Guardado datos_modificado.json")

    # 4. Convertir y guardar como datos.yaml usando pyyaml
    with open('datos.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
    print("Guardado datos.yaml")

if __name__ == '__main__':
    main()
