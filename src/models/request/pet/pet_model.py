from dataclasses import dataclass, asdict
from typing import Optional, List

from src.models.request.base_dataclass import BaseDataClass


@dataclass
class PetModel(BaseDataClass):
    id: Optional[int] = None
    name: Optional[str] = None
    photoUrls: Optional[List[str]] = None
    status: Optional[str] = None

    def as_list(self):
        obj_as_list = list()
        for key, value in asdict(self).items():
            if key == 'id':
                continue
            else:
                obj_as_list.append(value)
        return obj_as_list
