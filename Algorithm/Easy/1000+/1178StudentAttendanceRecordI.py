class Solution:
    """
    @param s: a string
    @return: whether the student could be rewarded according to his attendance record
    """

    def checkRecord(self, s):
        # Write your code here
        late = 0
        absent = 0
        for item in s:
            if item == 'A':
                absent += 1
                late = 0
            if item == 'L':
                late += 1
            if item == 'P':
                late = 0
            if absent > 1 or late > 2:
                return False
        return True
