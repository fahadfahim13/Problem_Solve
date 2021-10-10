import string
from typing import List, Callable
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
    def process_tickets(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass


def fifo_processing_strategy(inp_list: List[SupportTicket]) -> List[SupportTicket]:
    return inp_list.copy()


def filo_processing_strategy(inp_list: List[SupportTicket]) -> List[SupportTicket]:
    return list(reversed(inp_list.copy()))


def random_processing_strategy(inp_list: List[SupportTicket]) -> List[SupportTicket]:
    ans_list = inp_list.copy()
    random.shuffle(ans_list)
    return list(ans_list)


def blackhole_processing_strategy(inp_list: List[SupportTicket]) -> List[SupportTicket]:
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

    def process_tickets(self, processing_strategy_fn: Callable[[List[SupportTicket]], List[SupportTicket]]):
        print("Interview Strategy")
        temp_tickets = processing_strategy_fn(self.tickets)
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

    app.process_tickets(fifo_processing_strategy)
    app.process_tickets(filo_processing_strategy)
    app.process_tickets(random_processing_strategy)
    app.process_tickets(blackhole_processing_strategy)
