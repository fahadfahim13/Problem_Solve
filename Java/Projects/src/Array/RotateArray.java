package Array;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class RotateArray {

    public static void rotate(int[] nums, int k) {
        LinkedList<Integer> list = new LinkedList<Integer>();

        for (int num: nums) {
            list.add(num);
        }
        for (int i = 0; i < k; i++) {
            int num = list.removeLast();
            list.addFirst(num);
        }
        System.out.println(list);
    }

    public static void main(String[] args) {
        int[] arr = new int[]{1, 2, 3, 4, 5, 6, 7};

        int k = 3;
        rotate(arr, k);
    }
}
