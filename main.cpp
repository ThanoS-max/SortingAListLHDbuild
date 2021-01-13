#include <iostream>
#include <list>
#include <string>
using namespace std;
int main(){
  list<int> mylist{1,5,3,2,4,5,7,8,99,8,56,44,3,2};

  mylist.sort();
  
  for(auto it = mylist.begin(); it != mylist.end(); ++it)
  cout<<' '<< *it;
cout<<"\nSorting a string list: "<<endl;

list<string> mylist2{"hi" , "bye" , "thanks"};

mylist2.sort();

for(auto it2 = mylist2.begin(); it2 != mylist2.end(); it2++)
cout<<' '<<*it2;

  return 0;
}