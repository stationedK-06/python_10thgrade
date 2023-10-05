import java.util.Scanner; 

public class Runner 
{

	public static void main(String[] args) 
	{
		Scanner reader = new Scanner(System.in);
		
		System.out.print("Which program would you like to run? Choose either (1, 2): ");
		int choice = reader.nextInt(); 
		
		switch(choice) 
		{
			case 1: 
				LetterArtMaker.main(args);
				break; 
			case 2: 
				RectangleRoomArranger.main(args); 
				break; 
			default: 
				System.out.println("Error! Invalid Entry!");
				Runner.main(args);
		}
		
		System.out.println("Would you like to run another program? Y/N ");
		String response = reader.next(); 
		
		if(response.substring(0, 1).equals("Y") || response.substring(0, 1).equals("y"))
		{
			Runner.main(args);
		}
		else
		{
			System.out.println("Thank you for running me! ");
		}

	}

}
