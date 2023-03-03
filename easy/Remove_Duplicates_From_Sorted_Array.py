# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Given an integer array nums sorted in non-decreasing order, remove
# the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i +=1
        return len(nums)

# two pointers v 1
# Используйте медленный указатель, чтобы «заблокировать» «нужный» элемент,
# и используйте быстрый указатель, чтобы двигаться вперед по списку и искать
# новые уникальные элементы в списке. Или, другими словами, текущий медленный
# указатель используется для поиска последнего уникального номера результатов,
# а быстрый используется для итерации и обнаружения.
#
# Быстрое продвижение на каждой итерации, но медленное продвижение
# только тогда, когда два указателя находятся на двух разных элементах.
#
# Это означает, что элементы после nums[slow] и перед nums[fast] — это числа,
# которые мы видели раньше и которые больше не нужны (одна копия этих
# чисел уже сохранена перед текущим медленным (включительно)).
#
# Следовательно, чтобы это вновь обнаруженное (невидимое) число указывалось
# текущим быстрым в начало массива для окончательного ответа, нам просто
# нужно поменять местами это вновь обнаруженное число на место, которое
# следует за текущим медленным указателем, с одним из увиденных чисел
# (нам это все равно не нужно для ответа), а затем продвиньте медленный
# в той же итерации, чтобы заблокировать этот новый номер.

    def removeDuplicates_1(self, nums: list[int]) -> int:
        slow, fast = 0, 1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow + 1] = nums[fast]
                fast += 1
                slow += 1

        return slow + 1

# two pointers v 2
# Однако обратите внимание, быстрый указатель просто увеличивается на каждой
# итерации независимо от условий, это типичная работа цикла for.
# Следовательно, мы можем упростить эту «двухстрелочную» систему
# следующим образом:

    def removeDuplicates_2(self, nums: list[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
