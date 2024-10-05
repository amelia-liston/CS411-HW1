from typing import Optional

class MigrationPath:

     def __init__(self,
                species: str,
                start_location: Habitat,
                current_location: str,
                duration: Optional[int] = None) -> None:
        self.species = species
        self.current_location = current_location
        self.duration = duration
        # this is Pythonic for
        # if animals is not None:
        #   self.animals = animals
        # else:
        #   self.animals = []
        #self.animals = animals or []