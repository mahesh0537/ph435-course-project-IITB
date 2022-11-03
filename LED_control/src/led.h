#ifndef _led_h_
#define _led_h_

class Led {
    public:
        Led();
        void on(int brightness);
        void off();
        void blink(int delay_);
        void status();
    private:
		int _brightness;
		void set_pins();
		void brightness_to_pins();

};






#endif