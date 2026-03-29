import java.util.LinkedList;
import java.util.Queue;

/*
class Node
{
    int data;
    Node left, right;
    Node(int item)
    {
        data = item;
        left = right = null;
    }
}
*/

class Solution {
    void mirror(Node root) {
        // code here
        if (root == null) return;
        
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        
        while(!queue.isEmpty()){
            
            Node curr = queue.poll();
            
            
            Node temp = curr.left;
            curr.left = curr.right;
            curr.right = temp;
            
            if (curr.left != null) queue.add(curr.left);
            if (curr.right != null) queue.add(curr.right);
        }
        
    }
}