import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;

class StackOverflow extends UserProfileSO {
    String question;
    String question_link;
    String tags;
    int views;
    int no_of_answers;
    String user_id;
    String date_time;
    String user_link;
    String answer;
    String other;
    boolean valid;

    public StackOverflow() {
    }

    public StackOverflow(String question, String question_link, String tags, int views, int no_of_answers, String user_id, String date_time, String user_link, String answer) {
        this.question = question;
        this.question_link = question_link;
        this.tags = tags;
        this.views = views;
        this.no_of_answers = no_of_answers;
        this.user_id = user_id;
        this.date_time = date_time;
        this.user_link = user_link;
        this.answer = answer;
    }
}

class UserProfileSO {
    int gold;
    int silver;
    int bronze;

    public UserProfileSO() {
    }

    public UserProfileSO(int gold, int silver, int bronze) {
        this.gold = gold;
        this.silver = silver;
        this.bronze = bronze;
    }
}

class Operations {

    StackOverflow[] stackOverflows = new StackOverflow[5001];
    int position = 0;
    int index = 0;
    Map<String, ArrayList<Integer>> tag_map = new HashMap<>();

    void populateDetails() throws Exception {
        for (int z = 25145; z < 25245; z++) {
            String path = "src/sof-dataset/" + z + ".html";

            String data = "";
            data = new String(Files.readAllBytes(Paths.get(path)));


            int answers = 0;
            int view = 0;
            String link = "";
            String question = "";
            String tag = "";
            String date = "";
            String user_link = "";
            String user_id = "";
            String Answer = "";
            int go;
            int br;
            int si;

            int count = 0;
            String[] s = data.split("\n");
            for (int i = 0; i < s.length; i++) {
                s[i] = s[i].trim();
                int p = s[i].indexOf("id=\"question-summary-");
                if (p >= 0 && p < s[i].length()) {
                    count++;
                    String views = s[i + 10];
                    int v1 = views.indexOf("<strong>");
                    int v2 = views.indexOf("</strong>");
                    views = views.substring(v1 + 8, v2);
                    answers = Integer.parseInt(views);  //Answers
                    views = s[i + 13];
                    v1 = views.indexOf("title");
                    v2 = views.indexOf("views\">");
                    views = views.substring(v1 + 7, v2);
                    view = Integer.parseInt(views.strip().replace(",", "")); //views
                    String test = s[i + 18];
                    test = test.strip();
                    v1 = test.indexOf("a herf=\"");
                    v2 = test.indexOf("\" class");
                    test = test.substring(v1 + 14, v2);
                    test = "www.stackoverflow.com" + test;
                    link = test;     //link;
                    test = s[i + 18];
                    v1 = test.indexOf("-hyperlink\">");
                    v2 = test.indexOf("</a></h3>");
                    test = test.substring(v1 + 12, v2);
                    question = test;     //question
                    test = s[i + 20];
                }

                p = s[i].indexOf("class=\"tags");
                if (p >= 0 && p < s[i].length()) {
                    String test = s[i];
                    int v1 = s[i].indexOf("class=\"tags");
                    int v2 = s[i].indexOf("\">");
                    test = test.substring(v1 + 11, v2);
                    test = test.replace("t-", "");
                    tag = test;      //tags
                }
                p = s[i].indexOf("class=\"relativetime");
                if (p >= 0 && p < s[i].length()) {
                    int v1 = s[i].indexOf("relativetime\">");
                    int v2 = s[i].indexOf("</span>");
                    String test = s[i];
                    test = test.substring(v1 + 14, v2);
                    date = test;     //date
                }

                p = s[i].indexOf("class=\"excerpt\">");
                if (p >= 0 && p < s[i].length()) {
                    int pq = 1;
                    String test = "";
                    while (true) {
                        if (test.indexOf("</div>") >= 0) {
                            break;
                        } else {
                            if (s[i + pq].length() > 0) {
                                test = test + s[i + pq].strip();
                            }
                            pq++;
                        }
                    }
                    test = test.substring(0, test.length() - 6);
                    Answer = test;       //answer
                }

                p = s[i].indexOf("class=\"user-details");
                if (p >= 0 && p < s[i].length()) {
                    String test = s[i + 1];
                    int v1 = test.indexOf("<a herf=\"");
                    int v2 = test.indexOf("\">");
                    if (v2 >= 0) {
                        test = test.substring(v1 + 18, v2);
                        test = "www.stackoverflow.com" + test;
                    } else {
                        test = "";
                    }
                    user_link = test;        //user link
                    test = s[i + 1];
                    v1 = test.indexOf("\">");
                    v2 = test.indexOf("</a>");
                    if (v2 >= 0) {
                        test = test.substring(v1 + 2, v2);
                    } else {
                        test = test.strip();
                    }
                    user_id = test;      //user id
                    stackOverflows[index] = new StackOverflow(question, link, tag, view, answers, user_id, date, user_link, Answer);
                    index++;
                    position++;
                }

                p = s[i].indexOf("class=\"reputation-score\" title=\"reputation score \"");
                if (p >= 0 && p < s[i].length()) {
                    int g = s[i].indexOf("class=\"badge2\"");
                    int f;
                    if (g >= 0) {
                        String test;
                        test = s[i].substring(g + 47, g + 51);
                        f = test.indexOf("<");
                        test = test.substring(0, f);
                        si = Integer.parseInt(test);
                    } else {
                        si = 0;
                    }
                    g = s[i].indexOf("class=\"badge1\"");
                    if (g >= 0) {
                        String test;
                        test = s[i].substring(g + 47, g + 51);
                        f = test.indexOf("<");
                        test = test.substring(0, f);
                        go = Integer.parseInt(test);
                    } else {
                        go = 0;
                    }

                    g = s[i].indexOf("class=\"badge3\"");
                    if (g >= 0) {
                        String test;
                        test = s[i].substring(g + 47, g + 51);
                        f = test.indexOf("<");
                        test = test.substring(0, f);
                        br = Integer.parseInt(test);
                    } else {
                        br = 0;
                    }

                    stackOverflows[index - 1].gold = go;
                    stackOverflows[index - 1].silver = si;
                    stackOverflows[index - 1].bronze = br;
                }
            }
        }
    }

    void printDetails(int n) {
        for (int i = 0; i < n; i++) {
            System.out.println("Question: " + stackOverflows[i].question);
            System.out.println("Answer: " + stackOverflows[i].answer);
            System.out.println("Number of answers: " + stackOverflows[i].no_of_answers + "   Number of views: " + stackOverflows[i].views);
            System.out.println("User id: " + stackOverflows[i].user_id + "   User Badges: Gold " + stackOverflows[i].gold + " Silver " + stackOverflows[i].silver + " Bronze " + stackOverflows[i].bronze + ",   Date: " + stackOverflows[i].date_time);
            System.out.println();
        }
    }


    void badgePrinter(int gold, int silver, int bronze) {
        for (int i = 0; i < index; i++) {
            if (stackOverflows[i].gold == gold && stackOverflows[i].silver == silver && stackOverflows[i].bronze == bronze) {
                System.out.println(stackOverflows[i].views + "  " + stackOverflows[i].user_id + "  " + stackOverflows[i].date_time + "  " + stackOverflows[i].gold + " " + stackOverflows[i].silver + " " + stackOverflows[i].bronze);
            }
        }
    }

    void badgePrinter(int silver, int bronze) {
        for (int i = 0; i < index; i++) {
            if (stackOverflows[i].silver == silver && stackOverflows[i].bronze == bronze) {
                System.out.println(stackOverflows[i].views + "  " + stackOverflows[i].user_id + "  " + stackOverflows[i].date_time + "  " + stackOverflows[i].gold + " " + stackOverflows[i].silver + " " + stackOverflows[i].bronze);
            }
        }
    }

    void badgePrinter(int bronze) {
        for (int i = 0; i < index; i++) {
            if (stackOverflows[i].bronze == bronze) {
                System.out.println(stackOverflows[i].views + "  " + stackOverflows[i].user_id + "  " + stackOverflows[i].date_time + "  " + stackOverflows[i].gold + " " + stackOverflows[i].silver + " " + stackOverflows[i].bronze);
            }
        }
    }

    void insertingIntoMap() {
        for (int i = 0; i < index; i++) {
            String st = stackOverflows[i].tags;
            st = st.trim();
            String[] tags = st.split(" ");
            for (int j = 0; j < tags.length; j++) {
                if (tag_map.get(tags[j]) == null) {
                    ArrayList<Integer> user_list = new ArrayList<>();
                    user_list.add(i);
                    tag_map.put(tags[j], user_list);
                } else {
                    ArrayList<Integer> temp;
                    temp = tag_map.get(tags[j]);
                    temp.add(i);
                }
            }
        }

    }

    void printByTag(String tag) {
        ArrayList<Integer> temp;
        temp = tag_map.get(tag);
        if (temp == null) {
            System.out.println("Tag not found");
            return;
        }
        for (int i = 0; i < temp.size(); i++) {
            int k = temp.get(i);
            System.out.println("User id: " + stackOverflows[k].user_id + " \nQuestion: " + stackOverflows[k].question + " \nBadges " + stackOverflows[k].gold + " " + stackOverflows[k].silver + " " + stackOverflows[k].bronze);
        }
    }

    void printQuestionsOfTag(String str) {
        ArrayList<Integer> arr;
        arr = tag_map.get(str);
        System.out.println(arr.size());
        int[] arr1 = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            arr1[i] = arr.get(i);
        }
        printReleatedToTag(arr1, arr.size());
    }

    void printReleatedToTag(int[] arr1, int size) {
        for (int i = 0; i < size; i++) {
            for (int j = i + 1; j < size; j++) {
                if (stackOverflows[arr1[i]].gold < stackOverflows[arr1[j]].gold) {
                    int temp = arr1[i];
                    arr1[i] = arr1[j];
                    arr1[j] = temp;
                }
            }
        }
        for (int i = 0; i < size; i++) {
            if (stackOverflows[arr1[i]].gold != 0) {
                System.out.println(stackOverflows[arr1[i]].user_id + " (" + stackOverflows[arr1[i]].gold + ", " + stackOverflows[arr1[i]].silver + ", " + stackOverflows[arr1[i]].bronze + ")");
            }
        }
        for (int i = 0; i < size; i++) {
            for (int j = i + 1; j < size; j++) {
                if (stackOverflows[arr1[i]].silver < stackOverflows[arr1[j]].silver && stackOverflows[arr1[i]].gold == 0 && stackOverflows[arr1[j]].gold == 0) {
                    int temp = arr1[i];
                    arr1[i] = arr1[j];
                    arr1[j] = temp;
                }
            }
        }

        for (int i = 0; i < size; i++) {
            if (stackOverflows[arr1[i]].gold == 0 && stackOverflows[arr1[i]].silver != 0) {
                System.out.println(stackOverflows[arr1[i]].user_id + " (" + stackOverflows[arr1[i]].gold + ", " + stackOverflows[arr1[i]].silver + ", " + stackOverflows[arr1[i]].bronze + ")");
            }
        }
        for (int i = 0; i < size; i++) {
            for (int j = i + 1; j < size; j++) {
                if (stackOverflows[arr1[i]].bronze < stackOverflows[arr1[j]].bronze && stackOverflows[arr1[i]].gold == 0 && stackOverflows[arr1[j]].gold == 0 && stackOverflows[arr1[j]].silver == 0 && stackOverflows[arr1[i]].silver == 0) {
                    int temp = arr1[i];
                    arr1[i] = arr1[j];
                    arr1[j] = temp;
                }
            }
        }

        for (int i = 0; i < size; i++) {
            if (stackOverflows[arr1[i]].gold == 0 && stackOverflows[arr1[i]].silver == 0) {
                System.out.println(stackOverflows[arr1[i]].user_id + " (" + stackOverflows[arr1[i]].gold + ", " + stackOverflows[arr1[i]].silver + ", " + stackOverflows[arr1[i]].bronze + ")");
            }
        }
    }

    void printQuestionsOfTag(String[] str) {
        ArrayList<Integer> arr;
        arr = tag_map.get(str[0]);
        for (int i = 1; i < str.length; i++) {
            if (tag_map.get(str[i]) == null) {
                System.out.println("All tags not found");
                return;
            }
            arr.retainAll(tag_map.get(str[i]));
        }
        ArrayList<Integer> distct_arr = (ArrayList<Integer>) arr.stream().distinct().collect(Collectors.toList());
        int[] arr1 = new int[distct_arr.size()];
        for (int i = 0; i < distct_arr.size(); i++) {
            arr1[i] = distct_arr.get(i);
        }
        printReleatedToTag(arr1, distct_arr.size());
    }
}


public class StackOverflowData {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        Operations op = new Operations();
        op.populateDetails();
        op.insertingIntoMap();
        int p, gold, silver, bronze, n;
        System.out.println("Menu\n1. printing users\n2. print questions based on badges\n3. tag to print question\n4. Enter tags to print user_id and badges in ascending order");
        while (true) {
            System.out.println("Enter your choice");
            p = scan.nextInt();
            String tagg;
            switch (p) {
                case 1:
                    System.out.println("Enter no of questions to be printed");
                    n = scan.nextInt();
                    op.printDetails(n);
                    break;
                case 2:
                    System.out.println("Enter gold, silver and bronze badges");
                    gold = scan.nextInt();
                    silver = scan.nextInt();    //Method overloading can also be used
                    bronze = scan.nextInt();
                    op.badgePrinter(gold, silver, bronze);
                    break;
                case 3:
                    System.out.println("Enter the tag of the question");    //Question 3
                    scan.nextLine();
                    tagg = scan.nextLine();
                    op.printByTag(tagg);
                    break;
                case 4:
                    System.out.println("Enter tags separated by space");
                    scan.nextLine();
                    tagg = scan.nextLine();
                    tagg = tagg.trim();
                    String[] tags = tagg.split(" ");
                    if (tagg.length() == 1) {
                        op.printQuestionsOfTag(tags[0]);
                    } else {
                        op.printQuestionsOfTag(tags);
                    }
            }
        }
    }
}
