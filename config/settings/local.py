import environ

from .base import *  # noqa: F403,F401

env = environ.Env()

DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
