#include <iostream>
#include <vector>
#include <time.h>

#define UP 0
#define RIGHT 1
#define DOWN 2
#define LEFT 3

#define UP_ASCII 72
#define RIGHT_ASCII 77
#define DOWN_ASCII 80
#define LEFT_ASCII 75

using namespace std;

void Game();
void getUserInput(char*, bool*);
void addNextMove(vector<int>*);
void printArrow(const int);
void printMyVector(const vector<int>);

int main()
{
    system("color B");

    try
    {
        Game();
    }
    catch (const exception&)
    {
        cout << "Exeption EROR!!!!!!!!!!!!!!" << endl;
    }

    system("pause");
}


void Game()
{
    char userInput = ' ';
    bool firstFlag = true;
    vector<int> symonSequence = {};

    cout << "Welcome to Shumzy&Leib Symon!!!!" << endl;
    cout << R"(To play enter any key, to exit (any time) enter 'x':)" << endl;

    while (userInput != 'x')
    {
        getUserInput(&userInput, &firstFlag);
        addNextMove(&symonSequence);
        
    }
    printMyVector(symonSequence);
}

void getUserInput(char* userInput, bool* firstFlag)
{
    *userInput = _getwch();
        //cout << "your userInput is: " << userInput << endl;
        //cout << "your userInput is int : " << (int)userInput << endl;
        if ((int)*userInput == -32)
        {
            //cout << "Yoe Pressesd on Arrow!!!" << endl;
            *userInput = _getwch();
            //cout << "your Arrow is: " << (int)userInput << endl;
            
            switch (*userInput)
            {
            case UP_ASCII:
                printArrow(UP);
                break;

            case RIGHT_ASCII:
                printArrow(RIGHT);
                break;

            case DOWN_ASCII:
                printArrow(DOWN);
                break;

            case LEFT_ASCII:
                printArrow(LEFT);
                break;
            default:
                break;
            }

            *firstFlag = false;
        }
        else if(*userInput == 'x' || *firstFlag)
        {
            *firstFlag = false;
        }
        else
        {
            cout << R"(Press only on tha Arrows or 'x')" << endl;
        }
}

void addNextMove(vector<int>* symonSequence)
{
    int nextMove = rand() % 4;
    cout << "your next move is:" << nextMove << endl;
    symonSequence->push_back(nextMove);
}

void printArrow(const int arrow)
{
    switch (arrow)
    {
    case UP:
        cout << "    .    " << endl;
        cout << "  .:;:.  " << endl;
        cout << ".:;;;;;:." << endl;
        cout << "  ;;;;;  " << endl;
        cout << "  ;;;;;  " << endl << endl;
        break;

    case RIGHT:
        cout << "    ." << endl;
        cout << "....;;." << endl;
        cout << "::::;;;;." << endl;
        cout << "::::;;." << endl;
        cout << "    ." << endl << endl;
        break;

    case DOWN:
        cout << "  ;;;;;  " << endl;
        cout << "  ;;;;;  " << endl;
        cout << "..;;;;;.." << endl;
        cout << " ':::::' " << endl;
        cout << "   ':`   " << endl << endl;
        break;

    case LEFT:

        cout << "    ." << endl;
        cout << "  .;;...." << endl;
        cout << ".;;;;::::" << endl;
        cout << " ':;;::::" << endl;
        cout << "   ':" << endl << endl;
        break;

    default:
        cout << "ERORR!!!!!!!!!!!!!!!" << endl; 
        break;
    }
}

void printMyVector(vector<int> myVector)
{
    cout << "your vector is: ";
    for (vector<int>::iterator it = myVector.begin(); it != myVector.end(); ++it)
    {
        cout << *it << ", ";
    }
    cout << endl << endl;
}

