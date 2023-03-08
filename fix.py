import json

# Nombre del archivo JSON de entrada y de salida
input_file = 'villarreal.json'
output_file = 'virrarreal.json'

# Tabla de conversión de caracteres incorrectos a correctos
conversion_table = {
    'Гӯ': 'í',
    'Дұ': 'i', 
    'Г§': 'c',
    'Дҹ': 'g',
    'Гј': 'ü',
    'Г¶': 'o',
    'ГЎ': 'a',
    'Д°': 'I',
    'Гұ': 'ñ',
    'Еҹ': 'us',
    'ДҮ': 'c',
    'Г–': 'Ö',
    'ДҚ': 'c',
    'ЕӮ': 'l',
    'ГЈ': 'ã',
    'ГҰ': 'æ',
    'ЕЎ': 'š',
    'ГҮ': 'C',
    'ЕҪ': 'Z',
    'Г©': 'é',
    'ГӨ': 'ä',
    'Еҫ': 'z',
    'Еһ': 'S',
    'Гә': 'ú',
    'Е ': 'Š',
    'Е„': 'ń',
    'Гң': 'Ü',
    'Гі': 'ó',
    'ГҒ': 'Á',
    'Гҙ': 'ô',
    'Дғ': 'ă',
    'ГҪ': 'ý',
    'Ãģ': 'é',
    'Ãą': 'ñ',
    'TÃšnez': 'Túnez',
    'Ã“': 'Ó',
    'Ã¡': 'á',
    'Ã³': 'ó',
    'Ãº': 'ú',
    'Ã‰': 'É',
    'Ã­': 'í',
    'Ã‘': 'Ñ',
    'Ã¼': 'ü',
    'Ã‡': 'Ç',
    'Ã©': 'é',
    'Ã‰': 'É',
    'Ã‘': 'Ñ',
    'Ã¡': 'á',
    'Ã³': 'ó',
    'Ãº': 'ú',
    'Ã±': 'ñ',
    'Ã\xad': 'í',
    'Ã': 'Á',
    'Ã': 'Ó',
    'ÃĄ': 'á',
    'Ä': 'ć',
    'Ãš': 'ú',
    'Ä': 'č',
    'Å―': 'Ž',
    'ÃĐ': 'é',
    'Ã': 'É',
    'Ã ': 'á',
    # Agregar más caracteres incorrectos y sus correcciones aquí si es necesario
}

# Leer el archivo JSON de entrada
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Corregir los caracteres incorrectos en el archivo JSON
for item in data:
    for key, value in item.items():
        if isinstance(value, str):
            for incorrect_char, correct_char in conversion_table.items():
                value = value.replace(incorrect_char, correct_char)
            item[key] = value

# Escribir el archivo JSON corregido en el disco
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)