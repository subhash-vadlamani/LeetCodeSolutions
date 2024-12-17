class Solution {
    public ListNode partition(ListNode head, int x) {
      ListNode list1=new ListNode(0);
      ListNode start1=list1;
      ListNode temp=head;
      while(temp!=null){
        if(temp.val<x){
          list1.next=new ListNode(temp.val);
          list1=list1.next;
        }
        temp=temp.next;
      }
      ListNode list2=new ListNode(0);
      ListNode start2=list2;
      temp=head;
      while(temp!=null){
        if(temp.val>=x){
          list2.next=new ListNode(temp.val);
          list2=list2.next;
        }
        temp=temp.next;
      }
      list2.next=null;
      list1.next=start2.next;
      
      return start1.next;
        
    }
}