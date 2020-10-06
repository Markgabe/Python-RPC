import rpyc


class MyService(rpyc.Service):
    # código que é executado quando uma conexão é iniciada, caso seja necessário
    def on_connect(self, conn):
        pass

    # código que é executado quando uma conexão é finalizada, caso seja necessário
    def on_disconnect(self, conn):
        pass

    # este é um método exposto
    def exposed_get_answer(self):
        return 42

    exposed_the_real_answer_though = 43 # este é um atributo exposto

    def get_question(self): # este método não é exposto
        return "Qual é a cor do cavalo branco de Napoleão?"
    # Para iniciar o servidor


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()
