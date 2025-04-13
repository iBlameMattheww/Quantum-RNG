#include <stdio.h>
#include "pico/stdlib.h"

#define INPUT_PIN 2  // GPIO pin number
#define LED_PIN 3 // GPIO pin number for LED
#define POLLING_DELAY_US 9.5  // Polling delay in microseconds for estimated 17kHz signal
#define BUFFER_SIZE 1024

uint8_t buffer[BUFFER_SIZE]; 
volatile uint32_t bufferIndex = 0;
uint64_t totalBits = 0;

int main()
{
    stdio_init_all();
    gpio_init(INPUT_PIN);
    gpio_set_dir(INPUT_PIN, GPIO_IN);

    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);


    while (true) {  // Sample 100 million bits
        bool pinState = gpio_get(INPUT_PIN);
        buffer[bufferIndex ++] = pinState ? 1 : 0;  // Store 1 for high, 0 for low
        totalBits ++;

        if(bufferIndex >= BUFFER_SIZE) { // Buffer is full
            gpio_put(LED_PIN, 1); // Turn on LED
            for(uint32_t i = 0; i < BUFFER_SIZE; i++) {
                printf("%d", buffer[i]); // Send each bit as ASCII '0' or '1'
            }
            bufferIndex = 0; // Reset buffer index
            gpio_put(LED_PIN, 0); // Turn off LED
        }


        sleep_us(POLLING_DELAY_US); // Polling delay
    }


    return 0;
}
