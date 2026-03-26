//Driver Code Starts
import java.util.HashSet;

//Driver Code Ends
class Node {
    int data;
    Node next;

    Node(int x) {
        this.data = x;
        this.next = null;
    }
}

class GfG {
    static boolean detectLoop(Node head) {
        HashSet<Node> st = new HashSet<>();

        while (head != null) {

            // if this node is already present
            // in hashmap it means there is a cycle
            if (st.contains(head))
                return true;

            // if we are seeing the node for
            // the first time, insert it in hash
            st.add(head);

            head = head.next;
        }
        return false;
    }
//Driver Code Starts

    public static void main(String[] args) {

        Node head = new Node(1);
        head.next = new Node(3);
        head.next.next = new Node(4);

        head.next.next.next = head.next;

        if (detectLoop(head))
            System.out.println("true");
        else
            System.out.println("false");
    }
}
//Driver Code Ends