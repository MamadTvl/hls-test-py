from cmath import log
from time import sleep
import time
import requests
from src.request import RequestsClient


class Simulate:
    def __init__(self, segments, baseUrl, label) -> None:
        self.segments = segments
        self.baseUrl = baseUrl
        self.label = label
        self.length = len(segments)

    def run(self):
        fetchedDuration = 0
        sumOfResponseTime = 0
        countOfFailed = 0
        print(f'{self.label} | segments length: {self.length}')
        index = 0
        for segment in self.segments:
            if fetchedDuration >= 60:
                log('sleeping 30s')
                sleep(30)
                fetchedDuration = 0
            start = time.time()
            # print(f'{self.baseUrl}/{segment["uri"]}')
            res = requests.get(f'{self.baseUrl}/{segment["uri"]}')
            if not res.text:
                countOfFailed += 1
                print(f'{self.label} | failed')
            end = time.time()
            responseTime = end - start
            sumOfResponseTime += responseTime
            print(
                f'{self.label} | {index + 1}/{self.length} | time: {responseTime} s')
            fetchedDuration += segment['duration']
            index += 1
        print(f'{self.label} | avg: {sumOfResponseTime/self.length}')
        print(f'{self.label} | failed: {countOfFailed}')
