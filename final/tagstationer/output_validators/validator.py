import sys

indata = open(sys.argv[1], 'r')
require_unique = len(sys.argv) >= 4 and sys.argv[3] == 'require_unique'

N = int(indata.readline())
stations = []
for i in range(N):
  stations.append(map(int, indata.readline().split()))

f = open(sys.argv[2], 'r')
judge_answer = f.readline().strip()
answer = sys.stdin.readline().strip()
if not require_unique:
    if answer == "UNIK":
        answer = "JA"
    if judge_answer == "UNIK":
        judge_answer = "JA"

if answer != judge_answer:
  exit(43)

try:
  if answer == "JA" or answer == "UNIK":
    order = map(int,sys.stdin.readline().strip().split())
    if len(order) != N:
      exit(43)
    used = [False for i in order]
    curr = 0
    for station in order:
      station -= 1
      if station < 0 or station >= N or used[station]:
        exit(43)
      used[station] = True
      if stations[station][1] > curr:
        exit(43)
      curr -= stations[station][1]
      curr += stations[station][0]
    if curr != 0:
      exit(43)
except Exception:
  exit(43)

exit(42)
