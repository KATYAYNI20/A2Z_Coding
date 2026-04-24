class Solution:
    def whichWeekDay(self, day):
        match day:
            case 1:
                return "Monday"
            case 2:
                return "Tuesday"
            case 3:
                return "Wednesday"
            case 4:
                return "Thursday"
            case 5:
                return "Friday"
            case 6:
                return "Saturday"
            case 7:
                return "Sunday"
            case _:
                return "Invalid"


obj = Solution()
print(obj.whichWeekDay(3))  # Wednesday
print(obj.whichWeekDay(8))  # Invalid