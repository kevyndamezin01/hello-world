#ifndef _Temp_Header_
#define _Temp_Header_

#include "Arduino.h"

/*
Function: temp_initializer()
Description: This function will initialize the temperature sensor,
             into the correct configuration that the user will require.			 
*/
void temp_initializer();

/*
Function: define_addresses()
Description: This function will define all of the adresses needed,
             to programm the sensor.
*/
void define_addresses();

/*
Function: temp_header_setup()
Description: This function initializes pin's 5, 7, 11, 12,
             which is CS, MOSI, MISO, SLCK pins.
*/
void temp_pin_setup();

/*
Function: start_tx()
Description: This function will drive CS pin low. 
*/
void start_TX();

/*
Function: end_tx()
Description: This function will drive CS pin high. 
*/
void end_TX();

/*
Function: write_byte(byte data)
Description: This function will allow the user to write data,
             to a specific register.  
*/
void write_byte(byte data);

/*
Function: send_data(int data, int destination)
Description: This function will allow the user to send data to,
             a specific register of the temp sensor.   
*/
void send_data(int data, int destination);

/*
Function: reset_temp_sensor()
Description: This function will allow the user to reset,
             the temp sensor.   
*/
void reset_temp_sensor();

/*
Function: byte read_byte()
Description: This function will allow the user to read data that,
             the temp sensor will output.   
*/
byte read_byte();


// TEMPORARY -----------------------------------------------------


byte get_temp_temp();

void check_temp();

// ---------------------------------------------------------------
/*
Function: byte read_ID()
Description: This function will allow the user to retreive the,
             manufacture number of the device.    
*/
byte read_ID();

/*
Function: configure_temp_sensor()
Description: This function will configure the temp sensor to the,
             configuration address.    
*/
void configure_temp_sensor();

/*
Function: get_temp_readings()
Description: This function will allow the user to read the temperature,
             readings that the sensor is taking.     
*/
int get_temp_readings();

/*
Function: enable_1SPS_mode()
Description: This function will configure the temperature sensor to 1sps mode.     
*/
void enable_1SPS_mode();

/*
Function: enable_continuous_read_mode()
Description: This function will enable the temperature sensor's,
             continous read mode. Alllowing a constant stream of data.     
*/
void enable_continuous_read_mode();

/*
Function: enable_continuous_read_mode()
Description: This function will enable the temperature sensor's,
             continous read mode. Alllowing a constant stream of data.     
*/
void disable_continous_read_mode();

/*
Function: enable_shutdown_mode()
Description: This function will place the temp sensor into shutdown mode.     
*/
void enable_shutdown_mode();

/*
Function: disable_continuous_read_mode()
Description: This function will disable the temp sensors shutdown mode.     
*/
void disable_shutdown_mode();

/*
Function: process_uart_messages()
Description: This function will allow the script to process the commands that,
             the user is commanding.      
*/
void process_uart_messages();
#endif
