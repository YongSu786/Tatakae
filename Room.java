import java.util.Scanner: 
  public class Room{
      public static void main(string[]arrgs){
        final int floors = 5;
        final int rooms_per_floor = 4 
        boolean [][]rooms = new boolean [floors][rooms_per_floor};
        Scanner sc = new Scanner(System.in);
        int choice :
          do {
                System.out.println("------Hotel Room Booking System--------");
                System.out.println("1.View Room Status");
                System.out.println("2.Book A Room ");
                System.out.println("3.Exit");
                System.out.println("Enter Your Choice (1-3):");
                choice = Scanner .nextInt();
                Switch(choice){
                  case 1:
                    View Rooms(rooms):
                      break;
                  case 2:
                    book room(Rooms,Scanner);
                      break;
                  case 3:
                    System.out.println("Thank You For Using The Booking System!");
                      break:
                  default:
                    System.out.println("Invalid Choice , Enter Between 1-3"); }
                    }
                    }
                    while (choice!=3):
                    }
                      Scanner.close();
                      }
                       }
                       public static void book Room[boolean[][] rooms ,Scanner scanner )
                        {System.out.print("\n Enter Floor Number(1 to "+rooms.length+":");
                          int floor = Scanner.nextInt();
                            if(floor 
