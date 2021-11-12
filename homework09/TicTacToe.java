//package datastructures;

import java.util.Scanner;

public class TicTacToe{

	public static void print_board(char [][] board){

		for(int i = 0;i<3;i++)
		{
			System.out.println( " "+board[i][0] + " | " + board[i][1] + " | " + board[i][2]+" ");
			if(i ==2) break;
			System.out.println("---+---+---");
		}
	
	}
	
	public static int get_user_input(){
		Scanner scanner = new Scanner (System.in);
		System.out.print("Enter next move\n");  
		String user = scanner.next();
		return Integer.parseInt(user);
	}
	public static void play_move(char c, int p, char [][] board, int [] spot){
		
		switch(p){
			case 1:
				board[0][0] = c;
				spot[1] = 1;
				break;
			case 2:
				board[0][1] = c;
				spot[2] = 1;
				break;
			case 3:
				board[0][2] = c;
				spot[3] = 1;
				break;
			case 4:
				board[1][0] = c;
				spot[4] = 1;
				break;
			case 5:
				board[1][1] = c;
				spot[5] = 1;
				break;
			case 6:
				board[1][2] = c;
				spot[6] = 1;
				break;
			case 7:
				board[2][0] = c;
				spot[7] = 1;
				break;
			case 8:
				board[2][1] = c;
				spot[8] = 1;
				break;
			case 9:
				board[2][2] = c;
				spot[9] = 1;
				break;
		}		
	}
	public static void play_computer(char [][] board, int [] spots){
		int random;
		random = (int)(Math.random() * 9 + 1);
		while(spots[random] == 1 ){
			random = (int)(Math.random() * 9 + 1);
		}
		play_move('O', random, board, spots);
	}
	public static int check_board(char [][] board){
		char winner = ' ';
		int done = 1;
		for(int i =0; i<3;i++){
			if(board[i][0]==board[i][1]&&board[i][1]==board[i][2]&& board[i][2]!=' '){ 
				winner = board[i][0];
				done= 0;
				//System.out.println("opt 1");
			}
			if(board[0][i]==board[1][i]&&board[1][i]==board[2][i] && board[2][i]!=' '){ 
				winner = board[0][i]; 
				done= 0;
				//System.out.println("opt 2");

			}
		}
		if(board[0][0]==board[1][1]&&board[1][1]==board[2][2]&& board[2][2]!=' '){ 
			winner = board[0][0]; 
			done= 0;
			//System.out.println("opt 3");

		}
		if(board[0][2]==board[1][1]&&board[1][1]==board[2][0] && board[2][0]!=' '){ 
			winner = board[0][2]; 
			done= 0;
			//System.out.println("opt 4");
		}
		
		if(done == 0){
			if(winner == 'X'){
				System.out.println("Player 1 has won!");
			}else{
				System.out.println("Player 2 has won!");
			}
		}
		return done;

	}
	public static void main(String [] args){
		char[][] board = new char [3][3];
		int [] spots = new int[10];	
		for(int i = 0;i<3;i++)
		{
			for(int j = 0; j < 3; j++){
				board[i][j] = ' ';
				spots[(i+1)*(j+1)] = 0;
			}
		}
		int cont = 1;
		print_board(board);
		while(cont == 1){
			int m = get_user_input();
			while(spots[m] ==1){
				m = get_user_input();
			}
			play_move('X',m,board, spots);
			play_computer(board, spots);
			print_board(board);
			cont = check_board(board);
			
		}		
	}
}
