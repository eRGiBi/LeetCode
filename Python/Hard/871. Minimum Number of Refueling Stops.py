class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        r = []
        if startFuel >= target:
            return 0

        def dfs(cur_fuel, st_i, num_stops):
            if st_i < len(stations):
                if cur_fuel < 0:
                    r.append(-1)
                    # return -1
                    return
                print(st_i)
                if cur_fuel >= (target - (stations[st_i][0])):
                    r.append(num_stops)
                    # return num_stops
                    return

                for st in range(st_i, len(stations)):
                    dfs(cur_fuel, st + 1, num_stops)

                    dfs(cur_fuel + stations[st][1], st_i + 1, num_stops + 1)

        dfs(startFuel, 0, 0)

        valid_results = [x for x in r if x != -1]
        if not valid_results:
            return -1
        else:
            return min(valid_results)
