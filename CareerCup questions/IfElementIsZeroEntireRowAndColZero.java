public class IfElementIsZeroEntireRowAndColZero {

	// If any element in M*N Matrix is zero the entire row and Column should be
	// turned to 0
	public static void main(String args[]) {
		int a[][] = { { 0, 2, 3 }, { 4, 5, 6 }, { 7, 8, 0 } };
		int[] row_number = new int[9];
		int[] col_number = new int[9];

		// Printing the original Array\
		System.out.println("The original Array printed");
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				System.out.print(a[i][j]);
			}

			System.out.println();
		}

		// Iterating the data in the matrix and if zero found in any of the row
		// or column respective entry array is set
		int temp_var = 0;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {

				if (a[i][j] == 0) {
					row_number[temp_var] = i;
					col_number[temp_var] = j;
					temp_var++;
				}
			}
		}

		// Printing the corresponding row and column entries
		// Row entries

		for (int i = 0; i < temp_var; i++) {
			//if ((row_number[i] + col_number[i]) != 0) {

				// Setting up the row elements to zero

				for (int j = 0; j < 3; j++) {
					a[row_number[i]][j] = 0;
				}

				// Setting up the column elements to zero

				for (int j = 0; j < 3; j++) {
					a[j][col_number[i]] = 0;
				}
				// System.out.print(row_number[i]);
				// System.out.print(',');
				// System.out.print(col_number[i]);
				// System.out.println();
		//	}
		}

		// The modified array
		System.out.println("The modified array is ");

		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				System.out.print(a[i][j]);
			}
			System.out.println();
		}

	}

}
