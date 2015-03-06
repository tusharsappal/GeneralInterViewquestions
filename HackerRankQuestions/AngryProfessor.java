import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class AngryProfessor {
    public static void main(String args[]) throws NumberFormatException, IOException {
        int numOfTestCases = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // Taking input the number of the testCases

        numOfTestCases = Integer.parseInt(br.readLine());

        if (numOfTestCases > 10 && numOfTestCases < 1) {
            System.exit(1);
        } else {
            // Creating the result array to store the results of the computation

            String[] results = new String[numOfTestCases];
            // Now we have the test cases we wanted we will be computing further down

            for (int i = 0; i < numOfTestCases; i++) {
                int N, K;
                // Extracting the N and K values from the Input Given
                String[] NK = br.readLine().split("\\s+");
                N = Integer.parseInt(NK[0]);
                K = Integer.parseInt(NK[1]);

                if (N > 1000 && N < 1 && K < 1 && K > N) {
                    System.exit(1);
                } else {

                    String[] Ns = br.readLine().split("\\s+");
                    int counter = 0;
                    // first

                    for (int j = 0; j < Ns.length; j++) {
                        // Now we will be counting the number of early and ontime comers by traversing the array
                        // If the number of timely comers satisfy the condition , we will be going ahead with printing YES
                        // for the class to continue and NO for the class for not to be continued

                        if (Integer.parseInt(Ns[j]) <= 0) {
                            counter++;
                        } else {
                            continue;
                        }
                    }

                    if (counter < K) {
                        results[i] = "YES";
                    } else {
                        results[i] = "NO";
                    }

                }
            }

            // Printing the result
            for (String result : results) {
                System.out.println(result);
            }
        }

    }

}
