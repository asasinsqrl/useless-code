import random
def process(data):
    dataType = data['dataType']
    accessCount = data['accessCount']
    timestamp = data['timestamp']
    noisy_accessCount = min(max(accessCount + random.uniform(-0.5, 0.5), 1), 10)
    noisy_timestamp = min(max(timestamp + random.uniform(-0.5, 0.5), 0), 24)
    data['dataType'] = dataType / 2.0
    data['accessCount'] = noisy_accessCount / 10.0
    data['timestamp'] = noisy_timestamp / 24.0
    return data