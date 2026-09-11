class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []  #stack
        pair = []
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        
        
        for p,s in sorted(pair)[::-1]:
            time.append((target-p)/s)
            if len(time) > 1 and time[-1] <= time[-2]:
                time.pop()
        return len(time)
        