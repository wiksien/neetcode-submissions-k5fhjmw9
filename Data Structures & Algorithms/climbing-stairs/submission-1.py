class Solution:
    def climbStairs(self, n: int) -> int:
        visited = {}

        def countUnique(number_of_steps):
            if number_of_steps < 2:
                return 1
            
            if number_of_steps in visited:
                return visited[number_of_steps]

            total_count = countUnique(number_of_steps - 1) + countUnique(number_of_steps - 2)
            
            visited[number_of_steps] = total_count

            return total_count
        
        return countUnique(n)
        