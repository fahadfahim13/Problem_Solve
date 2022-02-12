import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class BinaryTreeInorderTraversal {
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> st = new Stack<TreeNode>();
        List<Integer> ans = new ArrayList<Integer>();
        while (!st.isEmpty() || root != null){
            while(root != null){
                st.push(root);
                root = root.left;
            }
            if(!st.isEmpty()){
                root = st.pop();
                ans.add(root.val);
                if (root.right != null) {
                    root = root.right;
                }
            }
            else{
                break;
            }
        }
        return ans;
    }

    public static void main(String[] args) {

    }
}
