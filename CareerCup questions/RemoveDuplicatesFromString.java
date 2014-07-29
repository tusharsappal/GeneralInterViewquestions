import java.util.Enumeration;
import java.util.Hashtable;

public class RemoveDuplicatesFromString {

	// This Program attempts to remove the duplicates from the string , using
	// the HashTable data structure
	@SuppressWarnings("unchecked")
	public static void main(String args[]) {

		String sample_string = "MISSISSIPPI";

		// Implement a HashMap and Store the individual chars in the Map on the
		// condition that we have not stored the
		// chars previously

		Hashtable<Character, Boolean> table = new Hashtable<Character, Boolean>();

		for (int i = 0; i < sample_string.length(); i++) {
			if (table.containsKey(sample_string.charAt(i))) {
				continue;
			} else {
				table.put(sample_string.charAt(i), true);
			}
		}

		// Now printing the count of individual data chars , duplicates removed

		System.out.println("Unique Characters are  " + table.size());
		Enumeration<Character> enumKeys = table.keys();
		while (enumKeys.hasMoreElements()) {
			Character key = enumKeys.nextElement();
			System.out.println("Keys are " + key);

		}

	}

}
