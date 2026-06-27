class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = []
        altitude.append(0)
        for index in range(len(gain)):
            ans = altitude[index] + gain[index]
            altitude.insert(index+1,ans)
        highest_altitude = max(altitude)
        return highest_altitude
