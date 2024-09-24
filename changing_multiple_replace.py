from re import sub, Match

PATH_ARQUIVO_ORIGINAL = "./arquivo.txt"
PATH_NOVO_ARQUIVO = "./arquivo-novo.txt"

replacements = {
    "foo": ["cat"],
    "bar": ["dog"]
}


def replace(match: Match[str]) -> str:
    return replacements[match.group(0)]


pattern = r"(foo|bar)"
buffer = []

with open(PATH_ARQUIVO_ORIGINAL, "r") as file:
    for line in file.readlines():
        buffer.append(sub(pattern, lambda match: replace(match), line))

with open(PATH_NOVO_ARQUIVO, "w") as file:
    for line in buffer:
        file.write(line)
