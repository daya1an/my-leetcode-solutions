/*
class Node
{
    int data;
    Node next;
    Node(int key)
    {
        data = key;
        next = null;
    }
}
*/

class Solution {
    public Node reverseKGroup(Node head, int k) {
        // code here
        if (head == null || k <= 1) return head;
        
        Node curr = head, prev = null;
        Stack<Node> stk = new Stack<>();
        
        while (curr != null){
            int count = 0;
            while (count<k && curr != null){
                stk.push(curr);
                count++;
                curr = curr.next;
            }
            
            while(!stk.isEmpty()){
                if (prev == null){
                    prev = stk.pop();
                    head = prev;
                }
                else{
                    prev.next = stk.pop();
                    prev = prev.next;
                }
            }
            prev.next = null;
        }
        
        return head;
    }
}