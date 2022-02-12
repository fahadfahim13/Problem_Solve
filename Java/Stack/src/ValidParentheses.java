import java.util.Stack;

public class ValidParentheses {
    // Leetcode 20: https://leetcode.com/problems/valid-parentheses/
    public static boolean isValid(String s){
        Stack<Character> st = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[') {
                st.push(s.charAt(i));
            }
            else if(s.charAt(i) == ')'){
                if (st.isEmpty() || st.peek() != '('){
                    return false;
                }
                st.pop();
            }
            else if(s.charAt(i) == '}'){
                if (st.isEmpty() || st.peek() != '{'){
                    return false;
                }
                st.pop();
            }
            else if(s.charAt(i) == ']'){
                if (st.isEmpty() || st.peek() != '['){
                    return false;
                }
                st.pop();
            }
        }
        return st.isEmpty();
    }

    public static void main(String[] args) {
        String s = "(}";
        System.out.println(isValid(s));
    }
}
