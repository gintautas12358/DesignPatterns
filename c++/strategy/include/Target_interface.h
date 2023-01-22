#ifndef TARGETINTERFACE_H
#define TARGETINTERFACE_H

class TargetInterface {
    public:
        virtual bool is_alive() = 0;
        virtual void modify_survivability(double modifier) = 0;
        virtual void got_shoted() = 0;
};

#endif