import string
from typing import List
import random


def generate_id(length=0):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue
