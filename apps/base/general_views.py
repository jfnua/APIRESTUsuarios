from dataclasses import dataclass

@dataclass
class ResponseGeneral:
  message: str
  data: object