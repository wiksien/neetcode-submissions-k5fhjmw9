class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        for temp_index in range(len(res) - 2, -1, -1):
            if temperatures[temp_index] < temperatures[temp_index + 1]:
                res[temp_index] = 1
            else:
                hottest_future_temp_index = temp_index + 1

                while temperatures[temp_index] >= temperatures[hottest_future_temp_index]:
                    if res[hottest_future_temp_index] == 0:
                        hottest_future_temp_index = temp_index
                        break
                    
                    hottest_future_temp_index += res[hottest_future_temp_index]
                
                res[temp_index] = hottest_future_temp_index - temp_index
            
        return res

