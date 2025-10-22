class ExtratorSimplesURL:
    def __init__(self, url):
        # Armazena a URL e faz uma verificação simples
        self.url = url.strip()
        self.valida_url()

    def valida_url(self):
        """Verifica se a URL está vazia"""
        if self.url == "":
            raise ValueError("A URL está vazia!")

    def get_valor_parametro(self, parametro):
        """Retorna o valor de um parâmetro dentro da URL"""
        # Encontra a posição do parâmetro
        indice_parametro = self.url.find(parametro)

        if indice_parametro == -1:
            return None  # parâmetro não encontrado

        # Posição onde o valor começa
        indice_valor = indice_parametro + len(parametro) + 1

        # Verifica se há outro parâmetro depois
        indice_e_comercial = self.url.find("&", indice_valor)

        if indice_e_comercial == -1:
            valor = self.url[indice_valor:]
        else:
            valor = self.url[indice_valor:indice_e_comercial]

        return valor




# Exemplo de uso:
url = "loja.com/produto?id=35&categoria=camisas&cor=azul"
extrator = ExtratorSimplesURL(url)

valor_quantidade = extrator.get_valor_parametro("id")
print("id:", valor_quantidade)