from dataclasses import dataclass
from faker import Faker


@dataclass
class User:
    username: str
    first_name: str
    last_name: str
    password: str
    email: str

    @staticmethod
    def create():
        return User(
            username=Faker().user_name(),
            first_name=Faker().first_name(),
            last_name=Faker().last_name(),
            password=Faker().password(),
            email=Faker().email()
        )
