import logging
from environs import Env
import json

from wildberies import WildberriesAPI

env = Env()
env.read_env()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    wb_token = env('WB_TOKEN')
    wb = WildberriesAPI(token=wb_token)
    res = wb.supply.acceptance_coefficients()

    print(json.dumps(res, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()