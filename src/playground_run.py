from run.simple_run import SimpleRun


class PlaygroundRun(SimpleRun):

    def __init__(self, log_dir: str):
        super().__init__(log_dir)
        self._events.before_run += lambda: print("BEFORE")
        self._events.after_run += lambda: print("AFTER")

    def _run(self, *arg, **kwargs):
        print("RUNNING")


if __name__ == '__main__':
    PlaygroundRun("/Users/bmeyer2/Desktop").run()
