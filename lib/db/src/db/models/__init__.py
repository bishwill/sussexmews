from .utils import merge_metadata
from .base import Base
from .public import Base as PublicBase
from .strava import Base as StravaBase


Base.metadata = merge_metadata(Base.metadata, PublicBase.metadata, StravaBase.metadata)
