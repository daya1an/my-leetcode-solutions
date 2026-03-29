class Node {
    int data;
    Node left, right;

    Node(int d)
    {
        data = d;
        left = right = null;
    }
}


class Solution {
    
    public int heightOf(Node curr){
        
        if (curr == null) return 0;
        
        return 1 + Math.max(heightOf(curr.left), heightOf(curr.right));
        
    }
    public boolean isBalanced(Node root) {
        // code here
        
        if (root == null) return true;
        
        int lh = heightOf(root.left);
        
        int rh = heightOf(root.right);
        
        // System.out.println(lh);
        
        // System.out.println(rh);
        
        if(Math.abs(lh - rh) > 1) return false;
        
        return isBalanced(root.left) && isBalanced(root.right);
        
    }
}