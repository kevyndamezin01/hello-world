#include "temp_header.h"
void temp_header_setup();

void setup() {
  // put your setup code here, to run once:
define_addresses();
temp_pin_setup();
temp_initializer();
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(1000);
  process_uart_messages();
}
