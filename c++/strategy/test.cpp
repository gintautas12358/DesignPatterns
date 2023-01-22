#include "Elk.h"
#include "Rifle.h"
#include "Hunting_odour.h"
#include "Hunter_game.h"
#include <iostream>

using namespace std;

int main() {

    Guninterface* gun = new Rifle();
    ToolInterface* tool = new HuntingOdour();
    TargetInterface* target = new Elk();
    HunterGame hg = HunterGame(gun, tool, target);

    hg.play();

    cout << "done" << endl;

    return 0;
}