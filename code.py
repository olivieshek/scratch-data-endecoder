# данная программа поможет закодировать строчные значения в числовые для того,
# чтобы была возможность применить ее, например, в глобальной переменной Scratch
# для сохранения результата (рейтинга) в игре.

alphabet = """абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\\"#$%&'()*+,-./:;<=>?@[]^_`{|}~ """
alphabet_digits = len(str(len(alphabet) - 1))

def encode(text: str) -> str:
    result = str()
    for i in text:
        try:
            idx = str(alphabet.index(i))
        except ValueError:
            print('Встретился символ не из алфавита,'
            ' в результате возвращен уже готовый результат.')
            return result
        if len(idx) == alphabet_digits:
            result += idx
        else:
            zeroes = alphabet_digits - len(idx)
            result += '0' * zeroes
            result += idx
    return result

def decode(code: str) -> str:
    result = str()
    iterator = 0
    for i in range(len(code) // alphabet_digits):
        try:
            idx = int(code[iterator:iterator + alphabet_digits])
        except ValueError:
            print('Символ(-ы) введенной строки'
            ' не входит(-ят) в цивровой ряд.')
            return str()
        result += alphabet[idx]
        iterator += alphabet_digits
    return result 
