from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository

db_connection_handler.connect_to_database()

def test_list_pets():
    repository = PetsRepository(db_connection_handler)
    response = repository.list_pets()
    print(response)