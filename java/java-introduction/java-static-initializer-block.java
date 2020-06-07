

static Scanner sc = new Scanner(System.in);
static int H = sc.nextInt();
static int B = sc.nextInt();
static boolean flag;
static {
    try {
        if(H>0 && B>0){
            flag = true;
        }
        else{
            throw new Exception("Breadth and height must be positive");
        }
    }
    catch (Exception e){
        System.out.println(e);
        }
    }




