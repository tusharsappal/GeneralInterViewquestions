public class isRotation {

	public static void main(String args[]) {
		String string1 = "waterbottle";
		String string2 = "erbottlewat";

		// Just follow the steps , check if the length of the two strings are
		// same
		// If same , concatenate string1 with itself and see that string
		// strings2
		// is a substring of string1
		if (string1.length() == string2.length()) {
			if (isSubString(string1 + string1, string2)) {
				System.out.println(string2 + " is a rotation of " + string1);
			} else {
				System.out
						.println(string2 + " is not a rotation of " + string1);
			}
		}

	}

	public static boolean isSubString(String string1, String string2) {
		if (string1.contains(string2)) {
			return true;
		} else
			return false;

	}

}
