import random
import math

# 해시 테이블 구현 (개방 주소법 - 선형 조사)
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash(self, key):
        return key % self.size

    def insert(self, key):
        idx = self.hash(key)
        probes = 0
        while self.table[idx] is not None:
            idx = (idx + 1) % self.size
            probes += 1
        self.table[idx] = key
        return probes + 1  # 자기 자신도 조사하므로 +1

    def search(self, key):
        idx = self.hash(key)
        probes = 1
        while self.table[idx] is not None:
            if self.table[idx] == key:
                return probes
            idx = (idx + 1) % self.size
            probes += 1
            if probes > self.size:  # 탐색 실패로 간주
                return probes
        return probes  # 탐색 실패

def simulate(m=1000, alpha=0.5, trials=100):
    n = int(m * alpha)
    results_success = []
    results_failure = []

    for _ in range(trials):
        # 무작위 키 생성
        keys = random.sample(range(10 * m), n)
        table = HashTable(m)
        
        for key in keys:
            table.insert(key)

        # 성공 검색: 테이블에 있는 키 중 무작위 선택
        success_key = random.choice(keys)
        probes_success = table.search(success_key)
        results_success.append(probes_success)

        # 실패 검색: 없는 키 생성
        while True:
            fail_key = random.randint(0, 10 * m)
            if fail_key not in keys:
                break
        probes_fail = table.search(fail_key)
        results_failure.append(probes_fail)

    avg_success = sum(results_success) / trials
    avg_failure = sum(results_failure) / trials

    # 이론값
    theory_fail = 1 / (1 - alpha)
    theory_success = (1 / alpha) * math.log(1 / (1 - alpha))

    return {
        'alpha': alpha,
        'avg_probes_success': avg_success,
        'theory_success': theory_success,
        'avg_probes_failure': avg_failure,
        'theory_failure': theory_fail
    }

# 시뮬레이션 실행
for alpha in [0.1, 0.3, 0.5, 0.7, 0.9]:
    result = simulate(alpha=alpha)
    print(f"[α={result['alpha']}]")
    print(f"  성공 평균 조사 횟수: {result['avg_probes_success']:.2f} (이론: {result['theory_success']:.2f})")
    print(f"  실패 평균 조사 횟수: {result['avg_probes_failure']:.2f} (이론: {result['theory_failure']:.2f})\n")
