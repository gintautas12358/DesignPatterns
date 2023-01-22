#include "Hunter_game.h"

using namespace std;

void HunterGame::play() {
    cout << 
    "\n " <<
    "###########   Game Starts   ########### \n" <<
    "\n" << endl;

    bool job_done = false;
    _tool->use(_target);
    _gun->load();
    for (int i = 0; i < 10; i++) {
        _gun->shoot(_target);
        if (!_target->is_alive()) {
            job_done = true;
            break;
        }
    }

    if (!job_done)
        cout << "Unlucky day :(" << endl;
    else
        cout << "Dinner will be served!" << endl;
}