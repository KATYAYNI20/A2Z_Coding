class Solution:
    def studentGrade(self, marks):
        if marks >= 90:
            return "Grade A"
        elif marks >= 70:
            return "Grade B"
        elif marks >= 50:
            return "Grade C"
        elif marks >= 35:
            return "Grade D"
        else:
            return "Fail"

obj = Solution()
print(obj.studentGrade(95))  # Grade A
print(obj.studentGrade(14))  # Fail