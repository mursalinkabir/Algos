public class TwoPointer {

	static int[] twopointer(int nums[], int target) {
		int i = 0, j = nums.length - 1;

		while (i < j) {
			//when the target is found
			if(nums[i]+nums[j]== target) {
				return new int[] { i, j };
			}
			
			//when the sum is smaller than target
			if(nums[i]+nums[j]< target) {
				i++;
			}
			
			//when the sum is greater than target
			else {
				j--;
			}
		}
		return new int[] { 0, 0 };

	}

	public static void main(String[] args) {
		 // array declaration
        int arr[] = { 3, 5, 9, 2, 8, 10, 11 };
         
        // value to search
        int val = 17;
        int ret[] =twopointer(arr,val);
        System.out.println("First index " + ret[0]+" Second Index "+ret[1]);
	}

}
