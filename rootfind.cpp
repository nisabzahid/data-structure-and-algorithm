#include <iostream>

using namespace std;

//finding the squire root of a number x throught binary search

double root(double x , double left, double right){
   
   double value=(left+right)/2.0;
        // as these are double type numbers, 
        //the difference between the given number x should be equal to the squir of the finding number 
    if(abs((value*value)-x) <= 10e-10)return value;
    else{
       
       if((value*value)<x )
            left= value+1;
        else right = value-1;
        //cout<<left<<" "<<right<<endl;
        
       return root(x, left , right);
    }
}

int main(){
    double x,y,left,right;
   while( cin>>x){
       
       if (x==0){cout<<0<<endl;continue;}
       if(x<0){cout<<"negetive number doesnot have sqrt;"<<endl;continue;}

        left =1.0,right = x;

    
    cout<<"squir root of : "<<x<<" : ";
    cout<<root(x,left,right);
    cout<<endl; 
   }
    return 0;
}