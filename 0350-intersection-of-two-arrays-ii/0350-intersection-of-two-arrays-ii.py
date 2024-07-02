class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        number_dict = {}
        
        for i in range(0, len(nums1)):
            if nums1[i] not in number_dict:
                number_dict[nums1[i]] = 1
            else:
                number_dict[nums1[i]] += 1
        
        intersection_list = []
        
        for i in range(0, len(nums2)):
            if nums2[i] in number_dict:
                intersection_list.append(nums2[i])
                number_dict[nums2[i]] -= 1
                if number_dict[nums2[i]] == 0:
                    number_dict.pop(nums2[i])
            
        return intersection_list