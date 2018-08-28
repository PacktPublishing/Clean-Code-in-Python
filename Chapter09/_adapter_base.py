from log import logger


class UsernameLookup:
    def search(self, user_namespace):
        logger.info("looking for %s", user_namespace)
