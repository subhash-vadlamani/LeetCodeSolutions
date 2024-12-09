class Solution {
    public int firstMissingPositive(int[] nums) {
        HashSet hs = new HashSet();
        int size = nums.length;
        for(int i=0;i<size;i++)
        {
            hs.add(nums[i]);
        }
        int missing = 1;
        for(int i = 1;i<=size;i++)
        {
            if(hs.contains(i))
            {
                missing = i+1;
                continue;
            }
            else
            {
                missing = i;
                break;
            }
        }
        return missing;
        
    }
}