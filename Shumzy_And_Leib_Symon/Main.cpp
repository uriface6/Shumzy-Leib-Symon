#include <iostream>

#define UP 0
#define RIGHT 1
#define DOWN 2
#define LEFT 3

using namespace std;

void Game();
void printArrow(const int);


int main()
{
    system("color B");

    cout << "Hello Symon" << endl << endl;
    printArrow(UP);
    printArrow(RIGHT);
    printArrow(DOWN);
    printArrow(LEFT);

    try
    {
        Game();
    }
    catch (const std::exception&)
    {

    }

    system("pause");
}


void Game()
{
    char flag = ' ';

    cout << "Welcome to Shumzy&Leib Symon!!!!" << endl;

    while (flag != 'x')
    {
        
        cout << R"(To play enter any key, to exit (any time) enter 'x':)" << endl;
        flag = _getwch();
        cout << "your flag is: " << flag << endl;
        cout << "your flag is int : " << (int)flag << endl;
        if ((int)flag == -32)
        {
            flag = _getwch();
            
        }
    }
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
        break;
    }
}

