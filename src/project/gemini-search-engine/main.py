import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Descarga los recursos de NLTK si es necesario
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')


class Documento:
    def __init__(self, id, contenido):
        self.id = id
        self.palabras = set(self.procesar_texto(contenido))

    def procesar_texto(self, texto):
        palabras = nltk.word_tokenize(texto.lower())
        stemmer = PorterStemmer()
        palabras_filtradas = [stemmer.stem(palabra) for palabra in palabras if
                              palabra not in stopwords.words('english')]
        return palabras_filtradas


# Índice invertido
indice_invertido = {}


def agregar_documento_al_indice(documento):
    for palabra in documento.palabras:
        if palabra not in indice_invertido:
            indice_invertido[palabra] = set()
        indice_invertido[palabra].add(documento.id)


def buscar(consulta):
    palabras_consulta = set(Documento("").procesar_texto(consulta))
    resultados = set()
    for palabra in palabras_consulta:
        if palabra in indice_invertido:
            resultados.update(indice_invertido[palabra])
    return resultados


if __name__ == "__main__":
    # Crear algunos documentos de ejemplo
    documentos = [
        Documento(1, "Este es el primer documento de ejemplo."),
        Documento(2, "Este es el segundo documento con algunas palabras repetidas."),
        # ... (agregar más documentos)
    ]

    # Crear el índice invertido
    for documento in documentos:
        agregar_documento_al_indice(documento)

    # Realizar una búsqueda
    resultados = buscar("primer document")
    print(resultados)
