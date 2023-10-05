import kareltherobot.*;

/*
 * Name: Joohan Kim
 * Period: 4th
 * Program #3
 * I didn't want to write 3 tureLeft to turnright                  
 */

public class RectangleRoomArranger {

	public static void main(String[] args) {
		World.setVisible(true);
		World.setDelay(1);
		// Change the path name to YOUR "s" number
		// "Unit2ProgramWorlds\\s******\\world3.kwld"
		UrRobot kim = new UrRobot(8, 2, Directions.East, 0);
		Robot senserk = new Robot(8, 2, Directions.East, 0);
		senserk.setVisible(false);
		World.readWorld("Unit2ProgramWorlds/s191267/world3.kwld");
		UrRobot joohan = new UrRobot(2, 3, Directions.East, 0);
		Robot senserj = new Robot(2, 3, Directions.East, 0);
		senserj.setVisible(false);
		for (int i = 0; i < 7; i++) {
			while (senserk.nextToABeeper() == true) {
				kim.pickBeeper();
			}
			for (int k = 0; k < 5; k++) {
				kim.move();
				senserk.move();
				while (senserk.nextToABeeper() == true) {
					kim.pickBeeper();
				}

			}
			if (i == 6) {
				turnRight(senserk, kim);
				for (int c = 0; c < 6; c++) {
					kim.move();
					senserk.move();
				}
				turnRight(senserk, kim);
				for (int c = 0; c < 5; c++) {
					kim.move();
					senserk.move();
				}
				turnRight(senserk, kim);
				break;
			}
			if (i % 2 == 0) {
				kim.turnLeft();
				senserk.turnLeft();
				kim.move();
				senserk.move();
				kim.turnLeft();
				senserk.turnLeft();
//
			} else {
				turnRight(senserk, kim);
				kim.move();
				senserk.move();
				turnRight(senserk, kim);
			}
		}

		for (int i = 0; i < 6; i++) {
			while (senserj.nextToABeeper() == true) {
				joohan.pickBeeper();
			}
			for (int k = 0; k < 6; k++) {
				joohan.move();
				senserj.move();
				while (senserj.nextToABeeper() == true) {
					joohan.pickBeeper();
				}
			}
			if (i == 5) {
				joohan.turnLeft();
				senserj.turnLeft();
				for (int c = 0; c < 5; c++) {
					joohan.move();
					senserj.move();
				}
				joohan.turnLeft();
				senserj.turnLeft();
				joohan.turnLeft();
				senserj.turnLeft();
				break;
			}
			if (i % 2 == 0) {
				joohan.turnLeft();
				senserj.turnLeft();
				joohan.move();
				senserj.move();
				joohan.turnLeft();
				senserj.turnLeft();

			} else {
				turnRight(senserj, joohan);
				joohan.move();
				senserj.move();
				turnRight(senserj, joohan);
			}
		}
		makeSquare(kim, senserk, 5, 5);
		makeSquare(joohan, senserj, 4, 3);

	}

	public static void turnRight(Robot senser, UrRobot name) {
		name.turnLeft();
		senser.turnLeft();
		name.turnLeft();
		senser.turnLeft();
		name.turnLeft();
		senser.turnLeft();
	}

//move one street or avenue and put beeper
	public static void moveAndPut(Robot senser, UrRobot name, int num) {
		for (int a = 0; a < num; a++) {
			name.move();
			senser.move();
			name.putBeeper();
		}
	}

	public static void makeSquare(UrRobot name, Robot senser, int x, int y) {
		turnRight(senser, name);
		moveAndPut(senser, name, x);
		name.turnLeft();
		senser.turnLeft();
		moveAndPut(senser, name, y);
		name.turnLeft();
		senser.turnLeft();
		moveAndPut(senser, name, x);
		name.turnLeft();
		senser.turnLeft();
		moveAndPut(senser, name, y);
		name.turnLeft();
		senser.turnLeft();
		name.move();
		senser.move();
		name.turnLeft();
		senser.turnLeft();
		name.move();
		senser.move();
		name.turnOff();
		senser.turnOff();

	}
}
