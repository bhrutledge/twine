from email import message
from typing import IO
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Union

def must_decode(value: Union[str, bytes]) -> str: ...
def parse(fp: IO[str]) -> message.Message: ...
def get(msg: message.Message, header: str) -> str: ...
def get_all(msg: message.Message, header: str) -> List[str]: ...

HeaderAttrs = Tuple[Tuple[str, str, bool], ...]
HEADER_ATTRS_1_0: HeaderAttrs
HEADER_ATTRS_1_1: HeaderAttrs
HEADER_ATTRS_1_2: HeaderAttrs
HEADER_ATTRS_2_0: HeaderAttrs
HEADER_ATTRS_2_1: HeaderAttrs
HEADER_ATTRS: Dict[str, HeaderAttrs]

class Distribution:
    # Required in all versions, but treated as optional by Distribution subclasses
    metadata_version: Optional[str]
    # version 1.0, PEP 241
    # Some attributes are non-optional because they're required in all versions,
    # and make downstream type annotations cleaner.
    name: str
    version: str
    platforms: Sequence[str]
    supported_platforms: Sequence[str]
    summary: str
    description: Optional[str]
    keywords: Optional[str]
    home_page: Optional[str]
    author: Optional[str]
    author_email: Optional[str]
    license: Optional[str]
    # version 1.1, PEP 314
    classifiers: Sequence[str]
    download_url: Optional[str]
    requires: Sequence[str]
    provides: Sequence[str]
    obsoletes: Sequence[str]
    # version 1.2, PEP 345
    maintainer: Optional[str]
    maintainer_email: Optional[str]
    requires_python: Optional[str]
    requires_external: Sequence[str]
    requires_dist: Sequence[str]
    provides_dist: Sequence[str]
    obsoletes_dist: Sequence[str]
    project_urls: Sequence[str]
    # version 2.1, PEP 566
    provides_extras: Sequence[str]
    description_content_type: Optional[str]
    def extractMetadata(self) -> None: ...
    def parse(self, data: Union[str, bytes]) -> None: ...
