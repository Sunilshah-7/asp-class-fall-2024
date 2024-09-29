#include <iostream>
#include <cmath>
#include <vector>
// a function which takes two integers and returns the prime numbers in between the range of them
void primeNumbers(int num1, int num2){

    // an array to store the prime numbers
    std::vector<int> primeNumbers;
    
    //find the minimum and maximum number and store in newNum1 and newNum2
    int newNum1 = num1 < num2 ? num1 : num2;
    int newNum2 = num1 > num2 ? num1 : num2;


    // check if the number is prime or not
    for(int i = newNum1; i <= newNum2; i++){
        bool isPrime = true;
        for(int j = 2; j <= sqrt(i); j++){
            if(i % j == 0){
                isPrime = false;
                break;
            }
        }
        if(isPrime){
           primeNumbers.push_back(i);
        }
    }
    // Print the prime numbers
    if(primeNumbers.size() == 0){
        std::cout << "No prime numbers found between "<< num1 << " and "<< num2 << "."<< std::endl;
        return;
    }
    std::cout <<"Prime numbers between "<< num1 << " and "<< num2 <<" are : ";
    for(int i = 0; i < primeNumbers.size(); i++){
        std::cout << primeNumbers[i] << " ";
    }
    std::cout << std::endl;
}

int main(){
    // take input from user and make sure it is a non zero positive number
    int num1, num2;
    do{
        std::cout << "Enter two non zero positive number separated by space: ";
        std::cin >> num1 >> num2;
    }while(num1 <= 0 || num2 <= 0);

    //function pointer for indirect call
    void (*funcPtr)(int, int);
    funcPtr = &primeNumbers;
    funcPtr(num1, num2);

    return 0;
}