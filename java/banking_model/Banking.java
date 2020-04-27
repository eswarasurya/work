class subAccounts {
    subAccounts.Savings s;
    subAccounts.Current c;
    subAccounts.FixedDeposit fixed;
    boolean isSavingsValid = false;
    boolean isCurrentValid = false;
    boolean isFDValid = false;

    class Savings extends Transaction {
        float balance;
        float interest;
    }

    class Current extends Transaction {
        float balance;
        float interest;
    }

    class FixedDeposit extends Transaction {
        float balance;
        float duration;   //Duration in years
        float interest;
    }
}

class Transaction {
    Transaction.Credit cred;
    Transaction.Debit debt;

    class Credit {
        int size = 0;
        float[] amount;
    }

    class Debit {
        int size = 0;
        float[] amount;
    }
}

class Profile extends subAccounts {
    String Name;
    String DoB;
    float balance;
    String pasportno;
    String personalno;
    String drivinglisence;
    String EmpId;
    int num;
    boolean valid = true;

    public Profile() {
    }

    public Profile(String name, String doB, float balance, String pasportno, String personalno) {
        Name = name;
        DoB = doB;
        this.balance = balance;
        this.pasportno = pasportno;
        this.personalno = personalno;
    }

    public Profile(String name, String doB, float balance, String pasportno, String personalno, String drivinglisence, String empId) {
        Name = name;
        DoB = doB;
        this.balance = balance;
        this.pasportno = pasportno;
        this.personalno = personalno;
        this.drivinglisence = drivinglisence;
        EmpId = empId;
    }

    public Profile(String name, String doB, float balance, String pasportno, String personalno, String drivinglisence) {
        Name = name;
        DoB = doB;
        this.balance = balance;
        this.pasportno = pasportno;
        this.personalno = personalno;
        this.drivinglisence = drivinglisence;
    }

    public Profile(String name, String doB, float balance, String pasportno) {
        Name = name;
        DoB = doB;
        this.balance = balance;
        this.pasportno = pasportno;
    }
}

class SpareBank {
    int n = 10;
    Profile[] cust = new Profile[n];

    void populatedetails() {
        int rand;
        int num;
        String custname;
        String DoB;
        int balance;
        String pasnum;
        String persnum;
        String Dlis;
        String empid;
        String[] name = {"Ram", "chand", "Stem", "Samey", "Krishna", "Sai", "Mani", "Eswara", "surat", "Ramonda", "vijay", "komal", "peru", "sami", "Tony"};
        String[] charset = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
        for (int i = 0; i < n; i++) {
            balance = 0;
            DoB = "";
            num = (int) (Math.random() * 4) + 1;
            rand = (int) (Math.random() * 15);
            custname = name[rand];
            rand = (int) (Math.random() * 31) + 1;
            DoB = DoB + (rand);
            rand = (int) (Math.random() * 13) + 1;
            DoB = DoB + "-" + (rand);
            rand = (int) (Math.random() * 36) + 1970;
            DoB = DoB + "-" + (rand);

            rand = (int) (Math.random() * 26);
            pasnum = charset[rand];
            rand = (int) (Math.random() * 8999998) + 1000000;
            pasnum = pasnum + rand;
            persnum = Integer.toString((int) (Math.random() * 8998) + 1000);
            persnum = persnum + " " + ((int) (Math.random() * 8998) + 1000);
            persnum = persnum + " " + ((int) (Math.random() * 8998) + 1000);
            Dlis = Integer.toString((int) (Math.random() * 899998) + 100000);
            Dlis = Dlis + "/" + ((int) (Math.random() * 98) + 1920);
            rand = (int) (Math.random() * 26);

            empid = charset[rand];
            rand = (int) (Math.random() * 26);
            empid = empid + charset[rand];
            rand = (int) (Math.random() * 26);
            empid = empid + charset[rand];
            rand = (int) (Math.random() * 26);
            empid = empid + charset[rand];
            rand = (int) (Math.random() * 88) + 11;
            empid = empid + rand;
            rand = (int) (Math.random() * 8998) + 1001;
            empid = empid + rand;
            if (num == 1) {
                cust[i] = new Profile(custname, DoB, balance, pasnum);
            } else if (num == 2) {
                cust[i] = new Profile(custname, DoB, balance, pasnum, persnum);
            } else if (num == 3) {
                cust[i] = new Profile(custname, DoB, balance, pasnum, persnum, Dlis);
            } else if (num == 4) {
                cust[i] = new Profile(custname, DoB, balance, pasnum, persnum, Dlis, empid);
            }
            cust[i].num = num;
            splitAccounts(i);
            if (cust[i].isSavingsValid) {
                balance = (int) cust[i].s.balance;
            }
            if (cust[i].isCurrentValid) {
                balance = balance + (int) cust[i].c.balance;
            }
            if (cust[i].isFDValid) {

                balance = balance + (int) cust[i].fixed.balance;
            }
            cust[i].balance = balance;
        }
    }

    void validteCostumers() {
        for (int i = 0; i < n; i++) {
            if (cust[i].balance < 5000) {
                cust[i].valid = false;
            } else {
                int year = Integer.parseInt(cust[i].DoB.substring(cust[i].DoB.length() - 4));
                if (2019 - year < 18) {
                    cust[i].valid = false;
                }
            }
        }
    }

    void printInvalidCostumers(){
        boolean isthere = false;
        System.out.println("\nInvalid costumers");
        for (int i = 0; i < n; i++) {
            if (cust[i].valid == false) {
                isthere = true;
                if (cust[i].num == 1) {
                    System.out.println(i + " Name: " + cust[i].Name + " DoB: " + cust[i].DoB + " Balance: " + cust[i].balance + " Passport number: " + cust[i].pasportno);
                } else if (cust[i].num == 2) {
                    System.out.println(i + " Name: " + cust[i].Name + " DoB: " + cust[i].DoB + " Balance: " + cust[i].balance + " Passport number: " + cust[i].pasportno + " Personal Number: " + cust[i].personalno);
                } else if (cust[i].num == 3) {
                    System.out.println(i + " Name: " + cust[i].Name + " DoB: " + cust[i].DoB + " Balance: " + cust[i].balance + " Passport number: " + cust[i].pasportno + " Personal Number: " + cust[i].personalno + " Driving licence: " + cust[i].drivinglisence);
                } else if (cust[i].num == 4) {
                    System.out.println(i + " Name: " + cust[i].Name + " DoB: " + cust[i].DoB + " Balance: " + cust[i].balance + " Passport number: " + cust[i].pasportno + " Personal Number: " + cust[i].personalno + " Driving licence: " + cust[i].drivinglisence + " Employee Id: " + cust[i].EmpId);
                }
            }
        }
        if (isthere == false) {
            System.out.println("There are no invalid costumers");
        }
    }

    void splitAccounts(int i) {
        int rand;
        int[] no;

        rand = (int) (Math.random() * 7) + 1;
        no = toBinary(rand);
        if (no[2] == 1) {
            cust[i].s = cust[i].new Savings();
            cust[i].s.balance = (int) (Math.random() * 10000) + 5000;
            cust[i].isSavingsValid = true;
        }
        if (no[1] == 1) {
            cust[i].c = cust[i].new Current();
            cust[i].c.balance = (int) (Math.random() * 10000) + 5000;
            cust[i].isCurrentValid = true;
        }
        if (no[0] == 1) {
            cust[i].fixed = cust[i].new FixedDeposit();
            cust[i].fixed.balance = (int) (Math.random() * 20000) + 10000;
            cust[i].fixed.duration = (int) (Math.random() * 3) + 1;
            cust[i].isFDValid = true;
        }
    }

    int[] toBinary(int a) {
        int[] n = new int[3];
        int i = 0;
        while (a > 0) {
            n[i] = a % 2;
            a = a / 2;
            i++;
        }
        return n;
    }

    void updateBalance(int i) {
        if (cust[i].isSavingsValid) {   //updating Savings
            for (int j = 0; j < cust[i].s.cred.size; j++) {
                cust[i].balance = cust[i].balance + cust[i].s.cred.amount[j];
                cust[i].s.balance = cust[i].s.balance + cust[i].s.cred.amount[j];
            }
            for (int j = 0; j < cust[i].s.debt.size; j++) {
                cust[i].balance = cust[i].balance - cust[i].s.debt.amount[j];
                cust[i].s.balance = cust[i].s.balance - cust[i].s.debt.amount[j];
            }
        }

        if (cust[i].isCurrentValid) {   //Updating current
            for (int j = 0; j < cust[i].c.cred.size; j++) {
                cust[i].balance = cust[i].balance + cust[i].c.cred.amount[j];
                cust[i].c.balance = cust[i].c.balance + cust[i].c.cred.amount[j];
            }
            for (int j = 0; j < cust[i].c.debt.size; j++) {
                cust[i].balance = cust[i].balance - cust[i].c.debt.amount[j];
                cust[i].c.balance = cust[i].c.balance - cust[i].c.debt.amount[j];
            }
        }

    }

    void createTransactions() {
        for (int i = 0; i < n; i++) {
            if (cust[i].isSavingsValid) {
                cust[i].s.cred = cust[i].s.new Credit();
                cust[i].s.cred.amount = new float[20];
                cust[i].s.cred.amount[cust[i].s.cred.size] = (int) (Math.random() * 5000) + 500;
                cust[i].s.cred.size++;
                cust[i].s.debt = cust[i].s.new Debit();
                cust[i].s.debt.amount = new float[20];
                cust[i].s.debt.amount[cust[i].s.debt.size] = (int) (Math.random() * cust[i].s.balance) + 100;
                cust[i].s.debt.size++;
            }
            if (cust[i].isCurrentValid) {
                cust[i].c.cred = cust[i].c.new Credit();
                cust[i].c.cred.amount = new float[20];
                cust[i].c.cred.amount[cust[i].c.cred.size] = (int) (Math.random() * 5000) + 500;
                cust[i].c.cred.size++;
                cust[i].c.debt = cust[i].c.new Debit();
                cust[i].c.debt.amount = new float[20];
                cust[i].c.debt.amount[cust[i].c.debt.size] = (int) (Math.random() * cust[i].c.balance) + 100;
                cust[i].c.debt.size++;
            }
        }
        for (int z = 0; z < n; z++) {
            updateBalance(z);
        }
    }

    void calucateInterest() { // Calculates interest for an account assuming interest period.
        for (int i = 0; i < n; i++) {
            if (cust[i].isSavingsValid) {
                cust[i].s.interest = (float) (cust[i].s.balance * (4.5 / 100));
                cust[i].s.balance = cust[i].s.balance + cust[i].s.interest;
                cust[i].balance = cust[i].balance + cust[i].s.interest;
            }
            if (cust[i].isCurrentValid) {
                cust[i].c.interest = (float) (cust[i].c.balance * (3.5 / 100));
                cust[i].c.balance = cust[i].c.balance + cust[i].c.interest;
                cust[i].balance = cust[i].balance + cust[i].c.interest;
            }
            if (cust[i].isFDValid) {
                cust[i].fixed.interest = (float) (cust[i].fixed.balance * (6.5 / 100));
                cust[i].fixed.balance = cust[i].fixed.balance + cust[i].fixed.interest;
                cust[i].balance = cust[i].balance + cust[i].fixed.interest;
            }
        }
    }

    void calculateTaxation() {
        for (int i = 0; i < n; i++) {
            if (cust[i].isSavingsValid) {
                cust[i].s.balance = cust[i].s.balance - genetareTaxAmount(cust[i].s.interest);
                cust[i].balance = cust[i].balance - genetareTaxAmount(cust[i].s.interest);
            }

            if (cust[i].isCurrentValid) {
                cust[i].c.balance = cust[i].c.balance - genetareTaxAmount(cust[i].c.interest);
                cust[i].balance = cust[i].balance - genetareTaxAmount(cust[i].c.interest);
            }

            if (cust[i].isFDValid) {
                cust[i].fixed.balance = cust[i].fixed.balance - genetareTaxAmount(cust[i].fixed.interest);
                cust[i].balance = cust[i].balance - genetareTaxAmount(cust[i].fixed.interest);
            }
        }
    }

    float genetareTaxAmount(float amount) {  //Calculates tax for a given amount
        float p;
        if (amount < 1000) {
            return 0;
        } else if (amount < 5000) {
            p = (float) amount * (float) 0.1;
            return p;
        } else if (amount < 10000) {
            p = (float) amount * (float) 0.2;
            return p;
        } else if (amount < 20000) {
            p = (float) amount * (float) 0.25;
            return p;
        } else if (amount < 50000) {
            p = (float) amount * (float) 0.5;
            return p;
        } else {
            p = (float) amount * (float) 0.5;
            return p;
        }
    }

    void printCostumers() {
        for (int i = 0; i < n; i++) {
            if (cust[i].valid == true) {
                if (cust[i].num == 1) {
                    System.out.println("\n"+i + " Name: " + cust[i].Name + " DoB: " + cust[i].DoB + " Balance: " + cust[i].balance + " Passport number: " + cust[i].pasportno);
                } else if (cust[i].num == 2) {
                    System.out.println("\n"+i + " Name: " + cust[i].Name + " DoB: " + cust[i].DoB + " Balance: " + cust[i].balance + " Passport number: " + cust[i].pasportno + " Personal Number: " + cust[i].personalno);
                } else if (cust[i].num == 3) {
                    System.out.println("\n"+i + " Name: " + cust[i].Name + " DoB: " + cust[i].DoB + " Balance: " + cust[i].balance + " Passport number: " + cust[i].pasportno + " Personal Number: " + cust[i].personalno + " Driving licence: " + cust[i].drivinglisence);
                } else if (cust[i].num == 4) {
                    System.out.println("\n"+i + " Name: " + cust[i].Name + " DoB: " + cust[i].DoB + " Balance: " + cust[i].balance + " Passport number: " + cust[i].pasportno + " Personal Number: " + cust[i].personalno + " Driving licence: " + cust[i].drivinglisence + " Employee Id: " + cust[i].EmpId);
                }
                if (cust[i].isSavingsValid && cust[i].s.balance<5000) {
                    System.out.println(" Savings " + cust[i].s.balance + "     Invalid Account");
                }
                else if(cust[i].isSavingsValid){
                    System.out.println(" Savings " + cust[i].s.balance + "  ");
                }
                if (cust[i].isCurrentValid && cust[i].c.balance<5000) {
                    System.out.println(" Current " + cust[i].c.balance+"    Invalid Account ");
                }
                else if(cust[i].isCurrentValid){
                    System.out.println(" Current " + cust[i].c.balance);
                }
                if (cust[i].isFDValid) {
                    System.out.println(" Fd " + cust[i].fixed.balance);
                }
            }
        }
    }

    void printCostumersTransactions() {
        for (int i = 0; i < n; i++) {
            if (cust[i].valid == true) {
                if (cust[i].num == 1) {
                    System.out.println("\n"+i + " Name: " + cust[i].Name + " DoB: " + cust[i].DoB + " Balance: " + cust[i].balance + " Passport number: " + cust[i].pasportno);
                } else if (cust[i].num == 2) {
                    System.out.println("\n"+i + " Name: " + cust[i].Name + " DoB: " + cust[i].DoB + " Balance: " + cust[i].balance + " Passport number: " + cust[i].pasportno + " Personal Number: " + cust[i].personalno);
                } else if (cust[i].num == 3) {
                    System.out.println("\n"+i + " Name: " + cust[i].Name + " DoB: " + cust[i].DoB + " Balance: " + cust[i].balance + " Passport number: " + cust[i].pasportno + " Personal Number: " + cust[i].personalno + " Driving licence: " + cust[i].drivinglisence);
                } else if (cust[i].num == 4) {
                    System.out.println("\n"+i + " Name: " + cust[i].Name + " DoB: " + cust[i].DoB + " Balance: " + cust[i].balance + " Passport number: " + cust[i].pasportno + " Personal Number: " + cust[i].personalno + " Driving licence: " + cust[i].drivinglisence + " Employee Id: " + cust[i].EmpId);
                }
                if (cust[i].isSavingsValid) {
                    System.out.print(" Savings Balance " + cust[i].s.balance + "  Credited Amounts ");
                    for (int k = 0; k < cust[i].s.cred.size; k++) {
                        System.out.print(cust[i].s.cred.amount[k] + " ");
                    }
                    System.out.print(" Debited Amounts ");
                    for (int k = 0; k < cust[i].s.debt.size; k++) {
                        System.out.print(cust[i].s.debt.amount[k] + " ");
                    }
                    System.out.println();
                }
                if (cust[i].isCurrentValid) {
                    System.out.print(" Current Balance " + cust[i].c.balance + " Credited Amounts ");
                    for (int k = 0; k < cust[i].c.cred.size; k++) {
                        System.out.print(cust[i].c.cred.amount[k] + " ");
                    }
                    System.out.print(" Debited Amounts ");
                    for (int k = 0; k < cust[i].c.debt.size; k++) {
                        System.out.print(cust[i].c.debt.amount[k] + " ");
                    }
                    System.out.println();
                }
                if (cust[i].isFDValid) {
                    System.out.print(" Fd balance " + cust[i].fixed.balance);
                    System.out.println();
                }

            }
        }
    }
}

public class Banking {
    public static void main(String[] args) {
        SpareBank bank = new SpareBank();

        bank.populatedetails();
        System.out.println("All Costumers");
        bank.validteCostumers();
        bank.printInvalidCostumers();
        System.out.println("\n\nValid Costumers");
        bank.printCostumers();

        bank.createTransactions();
        bank.validteCostumers();    //validating costumers after transactions
        System.out.println("\n\nPrinting transactions of the costumers");
        bank.printCostumersTransactions();
        bank.printInvalidCostumers();

        System.out.println("\n\nAfter adding interest");
        bank.calucateInterest();
        bank.printCostumers();

        System.out.println("\n\nAfter Deducting tax from the account ");
        bank.validteCostumers();
        bank.calculateTaxation();
        bank.printCostumers();
    }
}
