public class BinarySearch {

	int binarysearch(int arr[],int find) {
		int l=0,r = arr.length-1;
		
		while(l<=r) {
			
			//finding the middle element
			int m = l+(r-l)/2;
			//if middle element is same as the value is being searched.
			if(arr[m]== find)
				return m;
			//if the find value is smaller than middle element
			// the value must be on the left side of the array
			if(arr[m]> find) {
				r= m-1;
				
			}else {
				// the value must be on the right half of the array
				l= m+1;
			}
			
		}
		
		
		// if nothing is found
		return -1;

		
	}

	public static void main(String[] args) {

		BinarySearch bin = new BinarySearch();
		int arr[] = { 2, 3, 4, 10, 40 };
		//int n = arr.length;
		int x = 10;
		int res = bin.binarysearch(arr, x);
		if(res!= -1) {
			System.out.println("The value is present in the index "+res);
		}else {
			System.out.println("The value was not found ");
		}
	}

}
