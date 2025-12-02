import threading
import time
from queue import Queue
from typing import List


class Producer(threading.Thread):
    """
    Producer thread.
    Reads items from a source list and puts them into a shared Queue.
    After finishing, it inserts a poison pill to signal the consumer to stop .
    """

    def __init__(self, queue: Queue, source: List[str], poison_pill):
        super().__init__()
        self.queue = queue
        self.source = source
        self.poison_pill = poison_pill

    def run(self):
        # loop through source
        for item in self.source:
            print(f"Produced: {item}")
            # put into queue
            self.queue.put(item)
            # small delay to simulate realistic concurrency
            time.sleep(0.01)

        # send poison pill - signal the consumer that production
        self.queue.put(self.poison_pill)


class Consumer(threading.Thread):
    """
    Consumer thread.
    Reads items from a shared Queue and appends them to a destination list.
    Stops when it encounters the poison pill.
    """

    def __init__(self, queue: Queue, destination: List[str], poison_pill):
        super().__init__()
        self.queue = queue
        self.destination = destination
        self.poison_pill = poison_pill

    def run(self):
        while True:
            # take from queue
            item = self.queue.get()

            # break on poison pill
            if item is self.poison_pill:
                # Stop consuming
                break

            print(f"Consumed: {item}")
            # append to destination
            self.destination.append(item)
            time.sleep(0.01)

        # queue signalling
        self.queue.task_done()


def run_demo(source_data: List[str]) -> List[str]:
    """
    Runs a full producer-consumer pipeline.
    Creates queue, producer and consumer threads.
    Returns the destination list containing all consumed items
    """

    # check input
    if not isinstance(source_data, list):
        raise TypeError("source_data must be a list of strings.")

    if any(item is None for item in source_data):
        raise ValueError("source_data cannot contain None values.")

    # create queue, poison pill, destination
    q = Queue()
    destination = []
    poison_pill = object()

    # create threads
    producer = Producer(q, source_data, poison_pill)
    consumer = Consumer(q, destination, poison_pill)

    # start threads and join
    producer.start()
    consumer.start()

    # wait until the thread finishes
    producer.join()
    consumer.join()

    # return destination
    return destination


if __name__ == "__main__":
    # manual test
    sample_source = ["A", "B", "C", "D"]
    result = run_demo(sample_source)
    print("Final destination:", result)
