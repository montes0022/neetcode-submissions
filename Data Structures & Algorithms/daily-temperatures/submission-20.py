class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        holder = []


        for i in range(len(temperatures)):

            while holder and temperatures[i] > temperatures[holder[-1]]:
                day = holder.pop()
                output[day] = i - day

            holder.append(i)

        return output


        