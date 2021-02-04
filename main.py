import threading

from data_provider import *


def prepare_transports() -> List[Transport]:
    data_provider = DataProvider()
    # pack containers
    c1 = DeliveryContainer()
    c1.pack_container([data_provider.order_items[0],
                       data_provider.order_items[1],
                       data_provider.order_items[2],
                       data_provider.order_items[3],
                       data_provider.order_items[4]])
    c2 = DeliveryContainer()
    c2.pack_container([data_provider.order_items[5],
                       data_provider.order_items[6],
                       data_provider.order_items[7]])
    c3 = DeliveryContainer()
    c3.pack_container([data_provider.order_items[8],
                       data_provider.order_items[9],
                       data_provider.order_items[10],
                       data_provider.order_items[11]])
    c4 = DeliveryContainer()
    c4.pack_container([data_provider.order_items[12],
                       data_provider.order_items[13]])
    c5 = DeliveryContainer()
    c5.pack_container([data_provider.order_items[14],
                       data_provider.order_items[15]])
    # set up delivery orders
    o1 = DeliveryOrder([c1, c2], data_provider.accounts[0], data_provider.accounts[0].account_manager,
                       data_provider.addresses[0])
    o2 = DeliveryOrder([c3, c4], data_provider.accounts[1], data_provider.accounts[1].account_manager,
                       data_provider.addresses[1])
    o3 = DeliveryOrder([c5], data_provider.accounts[2], data_provider.accounts[2].account_manager,
                       data_provider.addresses[2])
    # set up transports
    t1 = Transport()
    t2 = Transport()
    t1.load([o1, o2])
    t2.load([o3])
    return [t1, t2]


def check_for_active_jobs(jobs: List[TransportJob]) -> bool:
    for job in jobs:
        if job.is_active:
            return True
    return False


if __name__ == "__main__":
    transports = prepare_transports()
    jobs = []
    for transport in transports:
        jobs.append(TransportJob(transport))
    for job in jobs:
        threading.Thread(target=job.execute).start()
    time.sleep(1)
    while check_for_active_jobs(jobs):
        info = "Transports in route | "
        for job in jobs:
            if job.is_active:
                info += f"Transport ID: {str(job.transport.transport_id).split('-')[0]}, " \
                        f"delivery ID: {job.current_delivery_id}, " \
                        f"destination: {job.transport.current_destination.city}, " \
                        f"progress: {job.transport.get_progress()} | "
        print(info)
        time.sleep(1)
