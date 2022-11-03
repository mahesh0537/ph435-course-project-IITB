#ifndef _led_h_
#define _led_h_

class Sensor {
    public:
        Sensor();
        int status();
    private:
		int _status;
        void read();


};






#endif