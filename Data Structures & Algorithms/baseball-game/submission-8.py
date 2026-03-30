class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        while operations:
            curr_op = operations.pop(0)

            if curr_op == "+":
                if len(record) < 1:
                    record.append(0)
                elif len(record) >= 2:
                    record.append(record[-2] + record[-1])
                continue
            
            if curr_op == "D":
                if len(record) < 1:
                    record.append(0)
                else:
                    record.append(record[-1] * 2)
                continue
            
            if curr_op == "C":
                if len(record) >= 1:
                    record.pop(-1)
                continue
            
            record.append(int(curr_op))
        
        return sum(record)

        