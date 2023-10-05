import kareltherobot.*;

/*
 * Name: Joohan Kim
 * Period: 4th
 * Program #1
 * Since my computer is macbook, directory is not same... \\for window, / for macbook                  
 */

public class LetterArtMaker {
	public static void main(String[] args) {
		World.setVisible(true);
		Robot senser = new Robot(1, 1, Directions.East, 0);
		senser.setVisible(false);
		UrRobot joohan = new UrRobot(1, 1, Directions.East, 0);
		World.setDelay(3);
		// Change the path name to YOUR "s" number
		// "Unit2ProgramWorlds\\s******\\world1.kwld"
		World.readWorld("Unit2ProgramWorlds/s191267/world1.kwld"); /* in mac book, folder\\folder\\file doesn't work */
		for (int i = 0; i < 10; i++) {
			for (int k = 0; k < 9; k++) {
				while (senser.nextToABeeper() == true) {
					joohan.pickBeeper();
				}
				joohan.move();
				senser.move();
			}
			if (i == 9) {
				joohan.turnLeft();
				senser.turnLeft();
				for (int c = 0; c < 9; c++) {
					joohan.move();
					senser.move();
				}
				joohan.turnLeft();
				senser.turnLeft();
				joohan.turnLeft();
				senser.turnLeft();
				break;
			}
			if (i % 2 == 0) {
				joohan.turnLeft();
				senser.turnLeft();
				joohan.move();
				senser.move();
				joohan.turnLeft();
				senser.turnLeft();

			} else {
				turnRight(senser, joohan);
				joohan.move();
				senser.move();
				turnRight(senser, joohan);
			}
		}

		for (int i = 0; i < 7; i++) {
			joohan.move();
			senser.move();
		}
		turnRight(senser,joohan);
		moveAndPut(senser, joohan, 4);
		turnRight(senser, joohan);
		moveAndPut(senser, joohan, 6);
		turnRight(senser, joohan);
		for (int i = 0; i < 3; i++) {
			joohan.move();
			senser.move();
			joohan.putBeeper();
			turnRight(senser, joohan);
			joohan.move();
			senser.move();
			joohan.putBeeper();
			joohan.turnLeft();
			senser.turnLeft();
		}
		joohan.move();
		senser.move();
		joohan.turnLeft();
		senser.turnLeft();
		for (int i = 0; i < 4; i++) {
			joohan.move();
		}
		joohan.turnLeft();
		senser.turnLeft();
		joohan.turnLeft();
		senser.turnLeft();
		joohan.turnOff();
		senser.turnOff();

	}
// TurnRight function
	public static void turnRight(Robot senser, UrRobot name) {
		World.setDelay(0);
		name.turnLeft();
		senser.turnLeft();
		name.turnLeft();
		senser.turnLeft();
		name.turnLeft();
		senser.turnLeft();
		World.setDelay(3);
	}
//move one street or avenue and put beeper
	public static void moveAndPut(Robot senser, UrRobot name, int num) {
		for (int a = 0; a < num; a++) {
			name.move();
			senser.move();
			name.putBeeper();
		}
	}
}
