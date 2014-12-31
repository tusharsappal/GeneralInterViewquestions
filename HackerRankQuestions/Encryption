import java.util.Scanner;


public class Encryption {
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);

        String stringToPlayWith = s.nextLine();
        stringToPlayWith = stringToPlayWith.replaceAll("\\s+", "");
        //System.out.println("trimmed String is "+ stringToPlayWith);

        if (stringToPlayWith.length() <= 81) {

            int rows = (int) Math.floor(Math.sqrt(stringToPlayWith.length()));
            int columns = (int) Math.ceil(Math.sqrt(stringToPlayWith.length()));

            //System.out.println("Columns are "+ columns +" and the rows are "+ rows);


            if (rows * columns >= stringToPlayWith.length()) {


                // Now the printing of the message starts

                int diff = rows * columns - stringToPlayWith.length();

                char a[][] = new char[rows][columns];
                String subStrArray[] = new String[rows];


                if (diff == 0) {


                    for (int i = 0; i < rows; i++) {


                        String subStr = stringToPlayWith.substring(i * columns, (i * columns) + columns);
                        //System.out.println(subStr);
                        subStrArray[i] = subStr;


                    }

                    for (int i = 0; i < rows; i++) {
                        for (int j = 0; j < columns; j++) {
                            if (subStrArray[i].charAt(j) == ' ') {
                                a[i][j] = ' ';
                            } else {
                                a[i][j] = subStrArray[i].charAt(j);
                            }

                        }
                    }


                    // Printing the array

                    for (int i = 0; i < columns; i++) {
                        for (int j = 0; j < rows; j++) {
                            System.out.print(a[j][i]);

                        }
                        System.out.print(" ");
                    }


                } else {
                    int endPoint = 0;
                    for (int i = 0; i < rows - 1; i++) {


                        String subStr = stringToPlayWith.substring(i * columns, (i * columns) + columns);
                        endPoint = (i * columns) + columns;
                        //System.out.println(subStr);
                        subStrArray[i] = subStr;
                    }

                    subStrArray[rows - 1] = stringToPlayWith.substring(endPoint, stringToPlayWith.length());
                    //System.out.println(stringToPlayWith.substring(endPoint, stringToPlayWith.length()));

                    for (int i = 0; i < rows - 1; i++) {
                        for (int j = 0; j < columns; j++) {
                            if (subStrArray[i].charAt(j) == ' ') {
                                a[i][j] = ' ';
                            } else {
                                a[i][j] = subStrArray[i].charAt(j);
                            }

                        }
                    }

                    for (int j = 0; j < columns - diff; j++) {
                        a[rows - 1][j] = subStrArray[rows - 1].charAt(j);
                    }


                    // Printing the array


                    for (int i = 0; i < columns; i++) {
                        String temp = "";
                        for (int j = 0; j < rows; j++) {
                            temp = temp + a[j][i];


                        }
                        System.out.print(temp.trim());
                        System.out.print(" ");
                    }


                }


                // Now storing the substrings in character two dimensional array


            } else {
                System.exit(1);
            }

        } else {
            System.exit(1);
        }


    }
}
