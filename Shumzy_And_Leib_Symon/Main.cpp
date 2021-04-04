#include <iostream>
#include <vector>
#include <time.h>
#include<windows.h>


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
void startNewGame(char*);
void getUserInput(char*);
void addNextMove(vector<int>*);
void move(char*, vector<int>*);
int arrowToInt(const char);
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
    vector<int> symonSequence = {};

    cout << "Welcome to Shumzy&Leib Symon!!!!" << endl;
    //cout << R"(To play enter any key, to exit (any time) enter 'x':)" << endl;

    while (userInput != 'x')
    {
        //getUserInput(&userInput, &firstFlag);
        //addNextMove(&symonSequence);
        startNewGame(&userInput);
        if (userInput == 'x')
        {
            break;
        }
        move(&userInput, &symonSequence);
    }
    //printMyVector(symonSequence);
}

void startNewGame(char* userInput)
{
    cout << "To start new game anter any key, to exit enter x (any time): " << endl;
    *userInput = _getwch();
}

void getUserInput(char* userInput)
{
    system("CLS");
    system("color B");

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
        }
        else
        {
            cout << R"(Press only on tha Arrows)" << endl;
        }
}

void addNextMove(vector<int>* symonSequence)
{
    int nextMove = rand() % 4;
    //cout << "your next move is:" << nextMove << endl;
    symonSequence->push_back(nextMove);
}

void move(char* userInput, vector<int>* symonSequence)
{
    bool endGame = false;
    int arrowInt = -1;

    addNextMove(symonSequence);

    while (!endGame)
    {
        printMyVector(*symonSequence);
        ///cout << "User:::::::::::" << endl;
        for (vector<int>::iterator it = symonSequence->begin(); it != symonSequence->end() && !endGame; ++it)
        {
            getUserInput(userInput);
            arrowInt = arrowToInt(*userInput);
            if (!(arrowInt == *it))
            {
                endGame = true;
                cout << "You Lose!!!!!!!!!" << endl;
                symonSequence->clear();
                break;
            }


        }
        if (!endGame) 
        { 
            addNextMove(symonSequence); 
        }
        system("CLS");
        Sleep(800);

    }
}

int arrowToInt(const char arrow)
{
    int returnInt = -1;

    switch (arrow)
    {
    case UP_ASCII:
        returnInt = UP;
        break;

    case RIGHT_ASCII:
        returnInt = RIGHT;
        break;

    case DOWN_ASCII:
        returnInt = DOWN;
        break;

    case LEFT_ASCII:
        returnInt = LEFT;
        break;

    default:
        cout << "ERORR!!!" << endl;
        break;
    }

    return returnInt;
}

void printArrow(const int arrow)
{
    system("CLS");
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
    system("CLS");
    system("color D");

    //cout << "Computer::::::::::::::::::::::::::::::::::" << endl;
    for (vector<int>::iterator it = myVector.begin(); it != myVector.end(); ++it)
    {
        //cout << *it << ", ";
       printArrow(*it);
       Sleep(500);
       system("CLS");
    }
}

