import java.util.Scanner;
public class Sudoku {

	public static void main(String[] args) {
		System.out.println("Hello, time to play sudoku ");
		int[][] data = new int[9][9];
		for(int i = 0;i<9;i++) {
			for(int j = 0;j<9;j++) {
				data[i][j] = -1;
			}
		}
		Scanner sc = new Scanner(System.in);
		//12int[] inputs = new int[9];
		boolean gameStatus = true ;
		String input;
		int counter = 0;
		int convert;
		int convert1;
		System.out.println("Put the inputs like, if row = 1 and you want to put input to 8 position the number 1 \n press 81 then space and \n 12 etc..");
		while(gameStatus) {
			System.out.printf("Whats the inputs at row %d put place and value \n", counter + 1 );
			input = sc.nextLine();
			input = input.replace(" ","");
			for(int k = 0; k < input.length(); k = k + 2) {
				convert = Integer.parseInt(String.valueOf(input.charAt(k)));
				convert1 = Integer.parseInt(String.valueOf(input.charAt(k+1)));
				//System.out.printf("%d %d \n",convert,convert1);
				data[counter][convert - 1] =  convert1;
				//System.out.printf("%d %d %d %d  \n" ,data[counter][convert],counter ,convert1,k );
			}
			counter++;
			if (counter ==  9) {
				SudokuInputs sn = new SudokuInputs(data);
				//sn.sudokuSolver();
				sn.show();
				System.out.println("do you want to try another sudoku  Y/N \n ");
				input = sc.nextLine(); // check here next time
				if(input.equals("Y")) {
					counter = 0;
				} else {
						gameStatus = false;
					}
				}
			}
		/*for(int i = 0; i < 9  ; i++) {
			for (int j = 0 ; j <9 ; j++) {
				System.out.printf("%d",data[i][j]);
			}
		System.out.println("");
 		}*/
	}
}


