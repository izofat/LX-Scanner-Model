import toml

config = toml.load("../config.toml")

DEBUG = config["debug"]
