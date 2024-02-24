from dataclasses import dataclass


@dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


gg = SimpleUser(
    full_name='Good Game',
    email='gg@goga.com',
    current_address="Good for good 123456",
    permanent_address="123456 GG perm address"
    )
