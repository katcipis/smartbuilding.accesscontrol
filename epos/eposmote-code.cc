#include <uart.h>

__USING_SYS

unsigned int *GPIO_BASE  = (unsigned int*) 0x80000000;
unsigned int *GPIO_BASE2 = (unsigned int*) 0x80000004;
unsigned int *GPIO_DATA = (unsigned int*) 0x8000000C;
unsigned int *GPIO_FUNCTION_SELECT   = (unsigned int*) 0x80000020;

bool open = false;

OStream cout;

void open_door() {
    // Sets bit on GPIO Pin 34
    *GPIO_DATA = 1 << 2;    

    // Green led (totally optional)
    *GPIO_BASE = 1 << 24;
    open = true;
}

void close_door() {
    // Unsets bit on GPIO Pin 34
    *GPIO_DATA = 0;    

    // Red led (totally optional)
    *GPIO_BASE = 1 << 23;
    open = false;
}

int main() {
    // Sets GPIO Pin 34 as output
    *GPIO_FUNCTION_SELECT = 48;
    *GPIO_BASE2 = 1 << 2;
    UART uart(0);
    *GPIO_BASE = 1 << 23;
    // Gets the signal which will be used for oppening the door 
    char open_code = uart.get();//0xff;//uart.get();
//    cout << "Open code: " << open_code << "\n";
    while(1){
        char c = uart.get();
//        cout << "Message received: " << c << "\n";        
        if (c == open_code)
        {
            if(!open)
                open_door();
        }
        else if(open)
            close_door();           
    }
}
