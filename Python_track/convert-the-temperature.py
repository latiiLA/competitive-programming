class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        temperature = []
        temperature.append(celsius + 273.15)
        temperature.append(celsius * 1.80 + 32.00)

        return temperature
