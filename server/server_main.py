import flwr as fl
from client.client import fit_config
from client_manager import RLManager
from evaluate import get_evaluate_fn
from dataset_utils import get_cifar_10

if __name__ == "__main__":

    num_rounds = 5 # 总共训练的几轮
    min_fit_clients = 2
    # configure the strategy
    train_path, testset = get_cifar_10()
    strategy = fl.server.strategy.FedAvg(
        fraction_fit=0.1,
        fraction_evaluate=0.1,
        min_fit_clients=min_fit_clients,
        min_evaluate_clients=min_fit_clients,
        on_fit_config_fn=fit_config,
        evaluate_fn=get_evaluate_fn(testset),  # centralised evaluation of global model
    )

    #
    # def client_fn(cid: str):
    #     # create a single client instance
    #     print("new client:{}".format(cid))
    #     return FlowerClient(cid, fed_dir)


    # (optional) specify Ray config
    # ray_init_args = {"include_dashboard": False}

    # start simulation
    # fl.simulation.start_simulation(
    #     client_fn=client_fn,
    #     num_clients=num_clients,
    #     client_resources=client_resources,
    #     config=fl.server.ServerConfig(num_rounds=num_rounds),
    #     strategy=strategy,
    #     ray_init_args=ray_init_args,
    #     client_manager=RLManager(),
    # )

    fl.server.start_server(
        config=fl.server.ServerConfig(num_rounds=num_rounds),
        strategy=strategy,
        client_manager=RLManager(),
    )

