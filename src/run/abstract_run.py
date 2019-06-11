import os
import sys
import time
from abc import abstractmethod, ABC
from typing import TypeVar, Generic, Callable

from events import Events

from util.std_out_to_file_logger import StdOutToFileLogger
from shutil import copyfile


T = TypeVar('T')


class AbstractRunEvents(Events):
    __events__ = ('before_run', 'after_run')

    def __init__(self) -> None:
        super().__init__()
        self.before_run: Callable[[], None] = self.before_run
        self.after_run: Callable[[T], None] = self.after_run


class AbstractRun(Generic[T], ABC):

    def __init__(self) -> None:
        self._start_timestamp = time.localtime()
        self._events = AbstractRunEvents()

    @property
    def start_time(self) -> str:
        return time.strftime('%Y_%m_%d__%H_%M_%S', self._start_timestamp)

    @property
    def code_file_name(self) -> str:
        file_name, file_extension = os.path.basename(self.file_path).split(r'.')
        return f'{file_name}_copy.{file_extension}'

    @property
    def output_file_name(self) -> str:
        return 'output.txt'

    @property
    @abstractmethod
    def root_log_dir(self) -> str:
        pass

    @property
    def run_name(self) -> str:
        return self.__class__.__name__

    @property
    def file_path(self) -> str:
        return sys.modules[self.__class__.__module__].__file__

    @property
    def run_log_dir(self) -> str:
        path = os.path.join(self.root_log_dir, self.run_name, self.start_time)
        return path

    def _copy_run_file(self) -> None:
        code_file_path = os.path.join(self.run_log_dir, self.code_file_name)
        assert not os.path.isfile(code_file_path), 'Code file must not exist.'
        copyfile(self.file_path, code_file_path)

    @abstractmethod
    def _run(self, *arg, **kwargs) -> T:
        pass

    def run(self, *arg, **kwargs) -> T:

        os.makedirs(self.run_log_dir, exist_ok=True)

        self._copy_run_file()

        output_file = os.path.join(self.run_log_dir, f"{self.output_file_name}")
        assert not os.path.isfile(output_file), "Output file must not exist."

        with StdOutToFileLogger(output_file):
            self._events.before_run()
            result = self._run(*arg, **kwargs)
            self._events.after_run()

        return result
