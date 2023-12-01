from .models import Item
from sqlmodel import Session


def create_item(session: Session, item: Item):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item
