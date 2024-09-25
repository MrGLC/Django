public class ArrayShift {

    public static void main(String[] args) {
        int[] array = {1, 4, 2, 5, 3, 5};  // Example array
        int numToReplace = 5;                // Number to replace
        int replacementValue = 8;            // Value to replace with

        shiftAndReplace(array, numToReplace, replacementValue);

        // Print the modified array
        System.out.println("Modified array:");
        for (int element : array) {
            System.out.print(element + " ");
        }
    }

    // Method to shift elements and replace the specified number
    public static void shiftAndReplace(int[] arr, int numToReplace, int replacementValue) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == numToReplace) {
                // Shift elements to the left
                for (int j = i; j < arr.length - 1; j++) {
                    arr[j] = arr[j + 1];
                }
                // Replace the last element
                arr[arr.length - 1] = replacementValue; 
                break; // Exit loop after replacing one instance (modify as needed)
            }
        }
    }
}
