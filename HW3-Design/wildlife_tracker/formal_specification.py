from typing import Any, List, Optional
from wildlife_tracker.animal_management.animal import Animal
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

age: Optional[int] = None #Animal
animal_id: int #Animal
animals: dict[int, Animal] = {} #Animal Manager
animals: List[int] = [] #Habitat
current_date: str #Migration
current_location: str #Migration
destination: Habitat #MigrationPath
duration: Optional[int] = None #MigrationPath
environment_type: str #Habitat
geographic_area: str #Habitat
habitat_id: int #Habitat
habitats: dict[int, Habitat] = {} #HabitatManager
health_status: Optional[str] = None #Animal
migration_id: int #Migration
migration_path: MigrationPath #Migration
migrations: dict[int, Migration] = {} #MigrationManager
path_id: int #MigrationPath and Migration
paths: dict[int, MigrationPath] = {} #MigrationManager
size: int #Habitat
species: str #MigrationPath
species: str #Animal
start_date: str #Migration
start_location: Habitat #MigrationPath
status: str = "Scheduled" #Migration


def assign_animals_to_habitat(animals: List[Animal]) -> None:
    pass #Habitat

def assign_animals_to_habitat(habitat_id: int, animals: List[Animal]) -> None:
    pass #Habitat

def cancel_migration(migration_id: int) -> None:
    pass #MigrationManager

def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
    pass #HabitatManager

def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
    pass #MigrationPath

def get_animal_by_id(animal_id: int) -> Optional[Animal]:
    pass #AnimalManager

def get_animal_details(animal_id) -> dict[str, Any]:
    pass #Animal

def get_animals_in_habitat(habitat_id: int) -> List[Animal]:
    pass #Habitat

def get_habitat_by_id(habitat_id: int) -> Habitat:
    pass #HabitatManager

def get_habitat_details(habitat_id: int) -> dict:
    pass #Habitat ***good example for type

def get_habitats_by_geographic_area(geographic_area: str) -> List[Habitat]:
    pass #HabitatManager

def get_habitats_by_size(size: int) -> List[Habitat]:
    pass #HabitatManager

def get_habitats_by_type(environment_type: str) -> List[Habitat]:
    pass #HabitatManager

def get_migration_by_id(migration_id: int) -> Migration:
    pass #Migration

def get_migration_details(migration_id: int) -> dict[str, Any]:
    pass #Migration

def get_migration_path_by_id(path_id: int) -> MigrationPath:
    pass #MigrationPath

def get_migration_paths() -> list[MigrationPath]:
    pass #MigrationPath

def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
    pass #MigrationPath

def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
    pass #MigrationPath

def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
    pass #MigrationPath

def get_migrations() -> list[Migration]:
    pass #Migration

def get_migrations_by_current_location(current_location: str) -> list[Migration]:
    pass #Migration

def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
    pass #Migration

def get_migrations_by_start_date(start_date: str) -> list[Migration]:
    pass #Migration

def get_migrations_by_status(status: str) -> list[Migration]:
    pass #Migration

def get_migration_path_details(path_id) -> dict:
    pass #MigrationPath

def register_animal(animal: Animal) -> None:
    pass #AnimalManager

def remove_animal(animal_id: int) -> None:
    pass #AnimalManager

def remove_habitat(habitat_id: int) -> None:
    pass #habitatManager

def remove_migration_path(path_id: int) -> None:
    pass #MigrationPath

def schedule_migration(migration_path: MigrationPath) -> None:
    pass #MigrationManager

def update_animal_details(animal_id: int, **kwargs: Any) -> None:
    pass #Animal

def update_habitat_details(habitat_id: int, **kwargs: dict[str, Any]) -> None:
    pass #Habitat

def update_migration_details(migration_id: int, **kwargs: Any) -> None:
    pass #Migration

def update_migration_path_details(path_id: int, **kwargs) -> None:
    pass #MigrationPath