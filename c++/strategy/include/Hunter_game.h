#include <iostream>
#include "Gun_interface.h"
#include "Tool_interface.h"
#include "Target_interface.h"

#ifndef HUNTINGGAME_H
#define HUNTINGGAME_H

class HunterGame {
    Guninterface* _gun;
    ToolInterface* _tool;
    TargetInterface* _target;

    public:
        HunterGame(Guninterface* gun, ToolInterface* tool, TargetInterface* target)
            : _gun(gun), _tool(tool), _target(target) {}
        
        void play();
};


#endif