import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class BinaryTreePreorderTraversal {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<Integer>();
        Stack<TreeNode> st = new Stack<TreeNode>();
        while(!st.isEmpty() || root != null){
            while (root != null) {
                ans.add(root.val);
                st.add(root);
                root = root.left;
            }
            root = st.pop();
            root = root.right;
        }
        return ans;
    }

    public static void main(String[] args) {

    }
}
