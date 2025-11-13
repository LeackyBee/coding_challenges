import sys

import requests
import orjson
import hashlib
import random

if __name__ == "__main__":
    access_token = input("Input access token:")
    data = requests.get(f"https://hackattic.com/challenges/mini_miner/problem?access_token={access_token}").text
    problem_json = orjson.loads(data)

    difficulty = problem_json["difficulty"]
    block = problem_json["block"]
    """
    block contains a nonce key, and a data key
    Aim is to find a value for nonce that makes the json-serialised sha256 hash of block have <difficulty> 0s in binary at the start
    This is HashCash - only solution is brute force, but there are many solutions so not a deep one
    """

    required_prefix = "0"*difficulty
    num = random.randint(0,sys.maxsize//2)
    while True:
        block["nonce"] = num
        test_str = orjson.dumps(block, option=orjson.OPT_SORT_KEYS)
        hash = hashlib.sha256(test_str).hexdigest()
        binary_hash = bin(int(hash, 16))[2:].zfill(256)
        if binary_hash[:difficulty] == required_prefix:
            print(f"Found nonce at {num}")
            break
        num += 1
    answer = orjson.dumps({"nonce": num})
    result = requests.post(f"https://hackattic.com/challenges/mini_miner/solve?access_token={access_token}&playground=1", answer)

    print(result.text)


