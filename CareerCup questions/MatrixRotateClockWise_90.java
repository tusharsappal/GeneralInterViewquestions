public class MatrixRotateClockWise_90 {

	public static void main(String args[]) {
		int a[][] = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };

		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				System.out.print(a[i][j]);

			}

			System.out.println();
		}

		System.out.println("------------------------------------");
		System.out.println("------------------------------------");

		rotateClockWise(a);

		System.out.println("------------------------------------");
		System.out.println("------------------------------------");

		rotateAntiClockWise(a);

	}

	private static void rotateAntiClockWise(int[][] a) {

		int row_upper_bound = 2;
		int col_upper_bound = 2;
		System.out.println("Rotating AntClockwise");
		for (int i = 0; i <= row_upper_bound; i++) {
			for (int j = 0; j <= col_upper_bound; j++) {
				System.out.print(a[j][col_upper_bound - i]);

			}

			System.out.println();
		}

	}

	private static void rotateClockWise(int[][] a) {

		int row_upper_bound = 2;
		int col_upper_bound = 2;

		System.out.println("Rotating Cockwise");
		for (int i = 0; i <= row_upper_bound; i++) {
			for (int j = 0; j <= col_upper_bound; j++) {

				System.out.print(a[row_upper_bound - j][i]);

			}

			System.out.println();
		}

	}

}
