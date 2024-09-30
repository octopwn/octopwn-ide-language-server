import enum
from _typeshed import Incomplete
from collections.abc import Generator

class ScanResult(enum.Enum):
    FINISHED = ...
    PROGRESS = ...
    RESULT = ...
    ERROR = ...

class ResultProgress:
    totalStages: Incomplete
    currentStage: Incomplete
    totalTargets: Incomplete
    finishedTargets: Incomplete
    def __init__(self, totalTargets, finishedTargets, totalStages, currentStage) -> None: ...
    def getPercentage(self): ...

class Result:
    tid: Incomplete
    target: Incomplete
    restype: Incomplete
    result: Incomplete
    total_targets: int
    def __init__(self, tid, target, restype, result: Incomplete | None = None) -> None: ...

class TargetListGen:
    targets: Incomplete
    def __init__(self) -> None: ...
    async def generate(self) -> Generator[Incomplete, None, None]: ...

class PortScanner:
    portranges: Incomplete
    worker_count: Incomplete
    proxies: Incomplete
    with_errors: Incomplete
    target_queue: Incomplete
    result_queue: Incomplete
    workers: Incomplete
    stop_evt: Incomplete
    timeout: Incomplete
    tgen_errors: Incomplete
    ports: Incomplete
    total_targets: int
    error_cnt: int
    finished_cnt: int
    prevpercentage: int
    target_generator_task: Incomplete
    def __init__(self, portranges: list[str], worker_count: int = 10, timeout: int = 5, proxies: Incomplete | None = None, with_errors: bool = False) -> None: ...
    async def stop(self) -> None: ...
    async def scan_target(self, tid, target, port) -> None: ...
    async def generate_targets(self): ...
    def calculate_ports(self) -> None: ...
    async def scan(self) -> Generator[Incomplete, None, None]: ...
