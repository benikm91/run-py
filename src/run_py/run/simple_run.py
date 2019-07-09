from abc import ABC

from run_py.run.abstract_run import AbstractRun


class SimpleRun(AbstractRun, ABC):

    def __init__(self, log_dir: str):
        super().__init__()
        self._log_dir = log_dir

    @property
    def root_log_dir(self) -> str:
        return self._log_dir
