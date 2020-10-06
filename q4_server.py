import time

import rpyc


class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_get_answer(self, vet):
        start = time.time()
        soma = sum(vet)
        end = time.time()
        print("Tempo de execução, em segundos, do procedimento no server: ", end - start)

        return soma


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()
