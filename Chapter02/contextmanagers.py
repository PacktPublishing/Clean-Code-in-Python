import contextlib


run = print


def stop_database():
    run("systemctl stop postgresql.service")


def start_database():
    run("systemctl start postgresql.service")


class DBHandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()


def db_backup():
    run("pg_dump database")


@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_database()


class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()

    def __exit__(self, ext_type, ex_value, ex_traceback):
        start_database()


@dbhandler_decorator()
def offline_backup():
    run("pg_dump database")


def main():
    with DBHandler():
        db_backup()

    with db_handler():
        db_backup()

    offline_backup()


if __name__ == "__main__":
    main()
