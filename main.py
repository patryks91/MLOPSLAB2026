import argparse
import os
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_path = f"config/.env.{environment}"
    load_dotenv(env_path)


def export_secret() -> None:
    with open("secret.yaml", encoding="utf-8") as file:
        secrets = yaml.safe_load(file)
        for name, value in secrets.items():
            os.environ[name] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secret()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY:", settings.API_KEY)
