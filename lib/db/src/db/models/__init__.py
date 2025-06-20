from .utils import merge_metadata
from .base import Base
from .public import Base as PublicBase
from .todo import Base as TodoBase


Base.metadata = merge_metadata(Base.metadata, PublicBase.metadata, TodoBase.metadata)
