import time
import rpyc
import sys


if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
conn = rpyc.connect(server, 18861)

n = input("Insira o número de elementos do vetor: ")

start = time.time()

vet = [i for i in range(int(n))]

print(conn.root)
print(conn.root.get_answer(vet))

end = time.time()

print(end - start)
