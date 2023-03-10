import time
import sys

sys.path.append("..")
from dataset_utils import get_cifar_10,do_fl_partitioning
import flwr as fl
from client import FlowerClient
from multiprocessing import Process

def start_client(cid:str,fed_dir:str):
    fl.client.start_numpy_client(server_address="[::]:9092", client=FlowerClient(cid, fed_dir))


if __name__ == "__main__":

    num_clients = 10
    fed_dir = "data/cifar-10-batches-py/federated"


    processes = list()
    for i in range(num_clients):
        print("start client {}".format(i))
        t = Process(target=start_client,args=(str(i),fed_dir))
        t.start()
        processes.append(t)
        time.sleep(5)

    for i in range(num_clients):
        processes[i].join()


