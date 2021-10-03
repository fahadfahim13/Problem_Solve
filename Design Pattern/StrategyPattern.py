import string
from typing import List
import random
from abc import ABC, abstractmethod


def generate_id(length=6):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class TicketProcessingStrategy(ABC):
    @abstractmethod
    def process_tickets(self, new_list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOProcessingStrategy(TicketProcessingStrategy):
    def process_tickets(self, new_list: List[SupportTicket]) -> List[SupportTicket]:
        return new_list.copy()


class FILOProcessingStrategy(TicketProcessingStrategy):
    def process_tickets(self, new_list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = new_list.copy()
        list_copy.reverse()
        return list_copy


class RandomProcessingStrategy(TicketProcessingStrategy):
    def process_tickets(self, new_list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = new_list.copy()
        random.shuffle(list_copy)
        return list_copy


class BlackHoleProcessingStrategy(TicketProcessingStrategy):
    def process_tickets(self, new_list: List[SupportTicket]) -> List[SupportTicket]:
        return []


class CustomerSupport:
    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_ticket(self, ticket: SupportTicket):
        print("====================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("====================")

    def process_tickets(self, processing_strategy: TicketProcessingStrategy):
        print("New Strategy")
        temp_tickets = processing_strategy.process_tickets(self.tickets)
        if len(temp_tickets) == 0:
            print("There are no tickets to process.")
        for i in temp_tickets:
            self.process_ticket(i)


if __name__ == "__main__":
    app = CustomerSupport()
    app.create_ticket("A", "issue 1")
    app.create_ticket("B", "issue 2")
    app.create_ticket("C", "issue 3")
    app.create_ticket("D", "issue 4")

    fifo_strategy = FIFOProcessingStrategy()
    filo_strategy = FILOProcessingStrategy()
    random_strategy = RandomProcessingStrategy()
    blackhole_strategy = BlackHoleProcessingStrategy()

    app.process_tickets(fifo_strategy)
    app.process_tickets(filo_strategy)
    app.process_tickets(random_strategy)
    app.process_tickets(blackhole_strategy)
