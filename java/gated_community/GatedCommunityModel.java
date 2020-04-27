import java.util.ArrayList;
import java.util.Scanner;

class GatedCommunity {
    String name;
    String location;
    float area;      //area in acres
}

class Blocks extends GatedCommunity {
    String blockName;
    int maxCapacity;
    String facing;
    Flats flats;
    Villas villas;
    PentHouse pentHouse;

    class Flats {
        int BedroomCount;
        int floor;
        String flatNo;
    }

    class Villas {
        String villaNo;
        float area;
    }

    class PentHouse {
        String houseName;
        String houseId;
    }
}


class SocialInfra extends GatedCommunity {
    int amount;
    String Organiser;
    String location;

    class Festivals {
        String name;
        String date;
        String temple;
    }

    class Event {
        String name;
        int participants;
        String date;
    }
}


class Market extends GatedCommunity {
    int costumerFrequency;
    int sales;
    String name;


    class Shops {
        ArrayList<String> items;
        String location;
        int size;   //small, large, medium
    }

    class Services {
        String seviceName;
        String serviceCategory;
        int rating;
    }
}

class Dwellers {
    String name;
    boolean gender;     //1. male, 2. female
    int age;
    String mobileNo;
    String email;
    String houseNo;
    int houseType;

    public Dwellers(String name, boolean gender, int age, String mobileNo, String email, String houseNo, int houseType) {
        this.name = name;
        this.gender = gender;
        this.age = age;
        this.mobileNo = mobileNo;
        this.email = email;
        this.houseNo = houseNo;
        this.houseType = houseType;
    }
}

class CulturalOrganisation extends SocialInfra{     //New class created by extending SocialInfra
    String orgId;
    String headName;
    ArrayList<Festivals> festivals = new ArrayList<>();
    ArrayList<Event> events = new ArrayList<>();

    public CulturalOrganisation() {
    }

    public CulturalOrganisation(String orgId, String headName, ArrayList<Festivals> festivals, ArrayList<Event> events) {
        this.orgId = orgId;
        this.headName = headName;
        this.festivals = festivals;
        this.events = events;
    }
}

class People {
    int n = 200;
    Dwellers[] dwellers = new Dwellers[n];
    int dwellsIndex = 0;
    Blocks[] blocks = new Blocks[n];
    CulturalOrganisation organisation;
    SocialInfra socialInfra = new SocialInfra();

    void populateDetails(int n) {

        String[] fname = {"emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Evelyn", "Abigail", "Harper", "Emily", "Elizabeth", "Avery", "Sofia", "Ella", "Madison", "Scarlett", "Victoria", "Aria", "Grace", "Chloe", "Camila", "Penelope", "Riley", "Layla", "Lillian", " Nora", " Zoey", "Mila", "Aubrey", "Hannah", "Lily", "Addison", "Eleanor", "Natalie", "Luna", "Savannah", "Brooklyn", "Leah", "Zoe", "Stella", "Hazel", "Ellie", "Puneeth"};
        String[] name = {"Ram", "chand", "Stem", "Samey", "Krishna", "Sai", "Mani", "Eswara", "surat", "Ramonda", "vijay", "komal", "peru", "sami", "Tony", "Zack ", "Arthur", "Hank ", "Rafael ", "Sackman ", "Aldridge", "Napoleon ", "Raymond", " Luke", "Baily ", "Barret ", "Bengt", "kashyap", "Gage"};
        String[] charset = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
        String[] num = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"};
        for (int i = 0; i < n; i++) {
            boolean gender = false;
            int rand, rand1;
            String phone = "";
            String tempname;
            String email;
            int age;
            int type;
            String houseId = "";
            if (dwellsIndex > n / 2) {
                rand = (int) (Math.random() * 45);
                tempname = fname[rand];
                rand = (int) (Math.random() * 45);
                tempname = tempname + " " + fname[rand];
                gender = false;
            } else {
                rand = (int) (Math.random() * 29);
                tempname = name[rand];
                rand = (int) (Math.random() * 29);
                tempname = tempname + " " + name[rand];
                gender = true;
            }
            rand = 10;
            while (rand > 0) {
                rand1 = (int) (Math.random() * 10);
                phone = phone + num[rand1];
                rand--;
            }
            age = (int) (Math.random() * 60) + 10;
            email = tempname.substring(0, 3) + tempname.substring(tempname.length() - 3) + "@gmail.com";

            if (dwellsIndex >= n / 2) {
                houseId = dwellers[dwellsIndex - 100].houseNo;
                type = dwellers[dwellsIndex - 100].houseType;
            } else {
                type = (int) (Math.random() * 3) + 1;
                rand = 6;
                while (rand > 0) {
                    rand1 = (int) (Math.random() * 26);
                    houseId = houseId + charset[rand1];
                    rand--;
                }
            }
            dwellers[dwellsIndex] = new Dwellers(tempname, gender, age, phone, email, houseId, type);
            dwellsIndex++;
        }
    }

    void printDwellerDeails() {
        for (int i = 0; i < dwellsIndex; i++) {
            printDweller(i);
        }

    }

    void divideBlocks() {
        for (int i = 0; i < dwellsIndex; i++) {
            blocks[i] = new Blocks();
            if (dwellers[i].houseType == 1) {
                blocks[i].flats = blocks[i].new Flats();
                blocks[i].flats.flatNo = dwellers[i].houseNo;
            } else if (dwellers[i].houseType == 2) {
                blocks[i].villas = blocks[i].new Villas();
                blocks[i].villas.villaNo = dwellers[i].houseNo;
            }

            if (dwellers[i].houseType == 3) {
                blocks[i].pentHouse = blocks[i].new PentHouse();
                blocks[i].pentHouse.houseId = dwellers[i].houseNo;
            }
        }
    }

    void giveAnnouncement(int a) {
        if (a == 1) {
            System.out.println("Announcing to all dwellers in Flats");
            for (int i = 0; i < dwellsIndex; i++) {
                if (blocks[i].flats != null) {
                    printDweller(i);
                }
            }
        } else if (a == 2) {
            System.out.println("Announcing to all dwellers in Villas");
            for (int i = 0; i < dwellsIndex; i++) {
                if (blocks[i].villas != null) {
                    printDweller(i);
                }
            }
        } else if (a == 3) {
            System.out.println("Announcing to all dwellers in Pent Houses");
            for (int i = 0; i < dwellsIndex; i++) {
                if (blocks[i].pentHouse != null) {
                    printDweller(i);
                }
            }
        }
        else if(a == 4){
            System.out.println("Announcing to all Dwellers");
            for(int i = 0;i<dwellsIndex/2;i++){
                printDweller(i);
                printDweller(i+100);
            }
        }
    }

    void giveAnnouncement(String str) {
        System.out.println("Pair lviing in house no: "+str);
        for (int i = 0; i < dwellsIndex; i++) {
            if (blocks[i].flats != null && blocks[i].flats.flatNo.equals(str)){
                printDweller(i);
            }
            else if(blocks[i].villas != null && blocks[i].villas.villaNo.equals(str)){
                printDweller(i);
            }
            else if(blocks[i].pentHouse != null && blocks[i].pentHouse.houseId.equals(str)){
                printDweller(i);
            }
        }
        System.out.println();
    }

    void printDweller(int i){
        System.out.println(i + " Name: " + dwellers[i].name + " Age: " + dwellers[i].age + " Mobile No: " + dwellers[i].mobileNo + " email: " + dwellers[i].email + " House Type: " + dwellers[i].houseType + " House No: " + dwellers[i].houseNo);
    }

    void generateCulturalOrganisation(){
        int rand = (int)(Math.random()*200);
        int rand1;
        String id = "";
        String name = dwellers[rand].name;
        String[] charset = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
        String[] fest = {"Makar Sakranti", "Pongal", "Basant Panchami", "Maha Shivratri", "Holi", "Baisakhi", "Bihu", "Eid Ul Fitr", "Hemis", "Rakshabandhan", "Janmashtmi", "Onam", "Ganesh Chaturthi", "Navratri", "Durga Puja", "Dussehra", "Diwali", "Gurupurab", "Christmas"};
        String[] eventsArr = {"Pranayama and Cleansing", "Ashtanga Yoga", "Philosophy & Discussion", "Yoga", "Teaching Methodology", "Anatomy and Physiology", " Iyengar Yoga", "Mantra Meditation", "National Science Day", "Friendship Day", "Easter", "Good Friday", "Womens Day", "Janmashtami"};
//        System.out.println(eventsArr.length);
        rand = (int)(Math.random()*3)+4;
        while (rand>0){
            rand1 = (int)(Math.random()*26);
            id = id + charset[rand1];
            rand--;
        }
        int festivalNumber = (int)(Math.random()*10)+5;
        int eventNumber = (int)(Math.random()*7)+4;
        ArrayList<SocialInfra.Festivals> festivals = new ArrayList<>();
        for(int i = 0;i<festivalNumber;i++){
            rand = (int)(Math.random()*19);

            SocialInfra.Festivals tempfest = socialInfra.new Festivals();
            tempfest.name = fest[rand];
            festivals.add(tempfest);
        }
        ArrayList<SocialInfra.Event> eventsList = new ArrayList<>();
        for(int i = 0;i<eventNumber;i++){
            rand = (int)(Math.random()*14);

            SocialInfra.Event tempEvents = socialInfra.new Event();
            tempEvents.name = eventsArr[rand];
            eventsList.add(tempEvents);
        }

        organisation = new CulturalOrganisation(id,name,festivals,eventsList);
    }

    void printFestivals(){
        System.out.println("Organised festivals are: ");
        for(int i = 0;i<organisation.festivals.size();i++){
            System.out.print(organisation.festivals.get(i).name+"  ");
        }
        System.out.println();
    }
    void printEvents(){
        System.out.println("Organised events are:");
        for(int i = 0;i<organisation.events.size();i++){
            System.out.print(organisation.events.get(i).name+"  ");
        }
        System.out.println();
    }

}


public class GatedCommunityModel {
    public static void main(String[] args) {
        People people = new People();
        Scanner scan = new Scanner(System.in);
        int n = 200;
        people.populateDetails(n);
        people.divideBlocks();
        System.out.println("Printing all Dweller details");
        people.printDwellerDeails();
        System.out.println("\nEnter 1. to give announcement to all flats\n      2. to to give announcement to all villas\n      3. to give announcement to all Penthouse\n      4.to give announcement to all Dwellers ");
        int p = scan.nextInt();
        people.giveAnnouncement(p);
        System.out.println("\nEnter house id of a Dweller to give announcement");
        scan.nextLine();
        String str = scan.nextLine();
        people.giveAnnouncement(str);
        System.out.println("Printing all festivals and events organised by a organisation");
        people.generateCulturalOrganisation();
        people.printFestivals();
        people.printEvents();
    }
}
