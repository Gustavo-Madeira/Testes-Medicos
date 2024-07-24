doencas = {
    "Gripe": ["febre", "tosse", "dor de garganta", "coriza", "dor no corpo"],
    "Covid-19": ["febre", "tosse", "falta de ar", "perda de olfato", "cansaço"],
    "Dengue": ["febre alta", "dor de cabeça", "dor atrás dos olhos", "dor nas articulações", "manchas na pele"],
    "Gastrite": ["dor abdominal", "azia", "náusea", "vômito", "sensação de estômago cheio"],
    "Amigdalite": ["dor de garganta", "febre", "dor ao engolir", "amígdalas inchadas", "mau hálito"],
    "Bronquite": ["tosse persistente", "produção de muco", "falta de ar", "fadiga", "desconforto no peito"],
    "Sinusite": ["dor de cabeça", "congestão nasal", "pressão facial", "corrimento nasal", "tosse"],
    "Hepatite": ["fadiga", "náusea", "vômito", "dor abdominal", "icterícia"],
    "Malária": ["febre alta", "calafrios", "suor", "dor de cabeça", "dor muscular"],
    "Pneumonia": ["febre", "calafrios", "tosse com catarro", "falta de ar", "dor no peito"],
    "Resfriado": ["coriza", "espirros", "tosse", "dor de garganta", "congestão nasal"],
    "Enxaqueca": ["dor de cabeça intensa", "náusea", "vômito", "sensibilidade à luz", "sensibilidade ao som"],
    "Cistite": ["dor ao urinar", "urgência urinária", "frequência urinária aumentada", "dor pélvica", "sangue na urina"],
    "Artrite Reumatoide": ["dor nas articulações", "rigidez matinal", "inchaço nas articulações", "fadiga", "perda de peso"],
    "Laringite": ["rouquidão", "dor de garganta", "tosse seca", "dificuldade para falar", "febre baixa"],
    "Otite": ["dor de ouvido", "perda auditiva", "febre", "secreção no ouvido", "dor de cabeça"],
    "Gastroenterite": ["diarreia", "náusea", "vômito", "dor abdominal", "febre"],
    "Anemia": ["fadiga", "fraqueza", "pele pálida", "falta de ar", "tontura"],
    "Hipertensão": ["dor de cabeça", "tontura", "fadiga", "dificuldade para respirar", "palpitações"],
    "Diabetes": ["sede excessiva", "urina frequente", "fome frenquente", "fadiga", "visão embaçada"],
}

def identificar_doenca(sintomas):
    possiveis_doencas = []
    for doenca, sintomas_doenca in doencas.items():
        if all(sintoma in sintomas_doenca for sintoma in sintomas):
            possiveis_doencas.append(doenca)
    return possiveis_doencas

sintomas_usuario = input("Digite os sintomas separados por vírgula: ").lower().split(", ")

doencas_encontradas = identificar_doenca(sintomas_usuario)

if doencas_encontradas:
    print("Possíveis doenças com base nos sintomas fornecidos:")
    for doenca in doencas_encontradas:
        print(f"- {doenca}")
else:
    print("Nenhuma doença encontrada com os sintomas fornecidos.")