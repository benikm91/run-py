from abc import ABC

from run.abstract_run import AbstractRun


class SimpleRun(AbstractRun, ABC):

    def __init__(self, log_dir: str):
        super().__init__()
        self._log_dir = log_dir

    @property
    def root_dir(self) -> str:
        return self._log_dir
