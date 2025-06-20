from .utils import merge_metadata
from .base import Base
from .public import Base as PublicBase


Base.metadata = merge_metadata(Base.metadata, PublicBase.metadata)
