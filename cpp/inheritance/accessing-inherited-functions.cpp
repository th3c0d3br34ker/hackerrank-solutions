

class D : public A, public B, public C
{
    int val;
    public:
        //Initially val is 1
        D()
        {
            val = 1;
        }


        //Implement this function
        void update_val(int new_val)
        {   while(new_val != 1) {
                if (new_val % 2 == 0) {
                    A :: func(val);
                    new_val /= 2;
                } else if (new_val % 3 == 0) {
                    B :: func(val);
                    new_val /= 3;
                } else {
                    C :: func(val);
                    new_val /= 5;
                } 
            }
        }
        //For Checking Purpose
        void check(int); //Do not delete this line.
};


