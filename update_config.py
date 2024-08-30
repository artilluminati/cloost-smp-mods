import os
import json

def update_launcher_json(launcher_path, mods_dir, resourcepacks_dir, shaderpacks_dir):
    # Чтение текущего launcher.json
    if os.path.exists(launcher_path):
        with open(launcher_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    else:
        print(f"Файл {launcher_path} не найден.")
        return

    # Получение списка всех файлов модов, ресурспаков и шейдеров
    mods = [f for f in os.listdir(mods_dir) if os.path.isfile(os.path.join(mods_dir, f))]
    resourcepacks = [f for f in os.listdir(resourcepacks_dir) if os.path.isfile(os.path.join(resourcepacks_dir, f))]
    shaderpacks = [f for f in os.listdir(shaderpacks_dir) if os.path.isfile(os.path.join(shaderpacks_dir, f))]

    # Обновление конфигурации
    config['mods'] = mods
    config['resourcepacks'] = resourcepacks
    config['shaderpacks'] = shaderpacks

    # Запись обновленного launcher.json
    with open(launcher_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
    print("Файл launcher.json успешно обновлен.")

# Пример использования
launcher_json_path = 'launcher.json'
mods_directory = 'mods'
resourcepacks_directory = 'resourcepacks'
shaderpacks_directory = 'shaderpacks'

update_launcher_json(launcher_json_path, mods_directory, resourcepacks_directory, shaderpacks_directory)
