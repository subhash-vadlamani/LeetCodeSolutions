class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> set=new HashSet<>();
         List<Integer>  result=new ArrayList<>();
        for(int x:nums) set.add(x);
        int count=1;
        while(count<=nums.length){
            if(!set.contains(count)) 
              result.add(count);
            count++;
        }
        return result;
    }
}