#include "Arduino.h"
#include "temp_header.h"
boolean rxComplete = false;
String inputString = "";
int debug = 0;
boolean continuous_mode_enabled = false;

 void define_addresses()
{
  #define CONFIGURATION_DATA 0x80
  #define CONFIGURATION_ADDR 0x01
  #define ENABLE_1SPS_MODE_DATA 0x40
  #define ENABLE_CONTINUOUS_READ_DATA 0x54
  #define DISABLE_CONTINUOUS_READ_DATA 0X50
  #define ENABLE_SHUTDOWN 0x60
  #define DISABLE_SHUTDOWN 0xC0
  #define ID_REGISTER_ADDR 0x03
}
 void temp_pin_setup()
{
  #define SCLK 7
  #define MISO 12
  #define MOSI 11
  #define CS 5
  #define LED 13
}
 void start_TX()
{
  // Drive CS low
  digitalWrite(CS, LOW);
}
 void end_TX()
{
  // Drive CS high
  digitalWrite(CS, HIGH);
}
 void enable_1SPS_mode()
{
  // Write 0x40 to register 0x01
  send_data(ENABLE_1SPS_MODE_DATA, CONFIGURATION_ADDR);
}
 void enable_continuous_read_mode()
{
  // Write 0x54 to register 0x01
  send_data(ENABLE_CONTINUOUS_READ_DATA, CONFIGURATION_ADDR);
  digitalWrite(MOSI, 0);
}  
 void disable_continuous_read_mode()
{
  // Write 0x50 to register 0x01
  send_data(DISABLE_CONTINUOUS_READ_DATA, CONFIGURATION_ADDR);
  
}
 
 void enable_shutdown_mode()
{
  // Write 0x60 to register 0x01
  send_data(ENABLE_SHUTDOWN, CONFIGURATION_ADDR); 
}
 void disable_shutdown_mode()
{
  // Write 0xC0 to register 0x01
  send_data(DISABLE_SHUTDOWN, CONFIGURATION_ADDR);
}
 void temp_initializer()
{
  Serial.begin(9600);
  // Serial.println("Temperautre Sensor!");
  // Set pins to correct starting values
  pinMode(SCLK, OUTPUT);
  pinMode(MISO, INPUT);
  pinMode(CS, OUTPUT);
  pinMode(MOSI, OUTPUT);
  // Initilaize pins as idle high
  digitalWrite(SCLK, HIGH);
  digitalWrite(MOSI, HIGH);
  //reset_temp_sensor();
  start_TX();
  configure_temp_sensor();
  end_TX();
  start_TX();
  read_ID();
  end_TX();
  start_TX();
  enable_continuous_read_mode();
  
//  start_TX();
//  enable_1SPS_mode();
//  end_TX();
}
 void process_uart_messages()
{  
  if(rxComplete == true)
  {
    rxComplete == false;
    if (debug == 1)
    {
      Serial.println("Message recived is: " + String(inputString));
    }
     if(inputString == "help")
    {
      Serial.println("This is your help message!");
      Serial.println("To begin a steam of data use 'help off'");
      Serial.println("To begin a steam of temperature readings use 'get temp'");
      Serial.println("To cancle the steam of temperature readings use 'stop temp'");
      Serial.println("To retrieve the manufacture number use 'get id'");
      Serial.println("To reset the temp sensor use 'reset'");
    }
     else if (inputString == "help off")
    {
      Serial.println("Finished with help message, turning debug back on!");
    }
     else if(inputString == "debug on")
    {
      debug = 1;
      Serial.println("Debug is on");
    }
     else if(inputString == "debug off")
    {
      debug = 0;
      Serial.println("Debug is off");
    }
     else if(inputString == "conf")
    {
        start_TX();
        //set_temp_sensor();
        enable_continuous_read_mode();
    }
     else if(inputString == "conf off")
    {
        end_TX();
    }
     else if(inputString == "get temp")
    {
        check_temp();               
    }
     else if(inputString == "reset")
    {
      reset_temp_sensor();
    }
     else if(inputString == "stop temp")
    {
      if(continuous_mode_enabled == true)
      {
        disable_continuous_read_mode();
        end_TX();
      }
    }
     else if(inputString == "turn temp off")
    {
      end_TX();
      disable_continuous_read_mode();
    }
     else if(inputString == "get id")
    {
      reset_temp_sensor();
      start_TX();
      read_ID();
      end_TX();
    }
     else if(inputString == "x")
    {
      start_TX();
      get_temp_temp();
      end_TX();
    }
    inputString = "";
  }
}
 void serialEvent()
{
  while( Serial.available())
  {
    char rx_in = (char)Serial.read();
    if (rx_in == '\n')
    {
      rxComplete = true;
    }
    else
    {
      inputString += rx_in;
    }
  }
}
 void write_byte(byte data)
{
  // Send MSB first
  
  // For each BIT in DATA: 
  for( int i = 7; i > -1; i--)
  {
    // Put BIT on MOSI
    digitalWrite(MOSI, bitRead(data, i));
     // Setup delay
   delay(1/1000);
     // Take SCLK high
    digitalWrite(SCLK, HIGH);
    
    // Hold delay 
   delay(1/1000);
    
    // Take SCLK low
    digitalWrite(SCLK, LOW);
  }
}
 void send_data(int data, int destination)
{
  // Transmit the DATA to the DESTINATION
   // Transmit each BIT of DESTINATION
  write_byte(destination);
   // Transmit each BIT of DATA
  write_byte(data);
   digitalWrite(MOSI, HIGH);
}
 void reset_temp_sensor()
{
  digitalWrite(CS, LOW);
  
    // ADDT0170 will reset if 32 consecutive 1's are transmitted
    for (int i = 0; i < 4; i++)
    {
      write_byte(0xFF);
    }
  digitalWrite(CS, HIGH);
}
 byte read_byte()
{
  byte rx_byte = 0x00;
  
  for(int i = 7; i > -1; i--)
  {
    // Setup time  
   delay(1/1000);
    
    // Read bit from DOUT
    rx_byte |= (digitalRead(MISO) << i);
    //Serial.println("Read bit: " + String(digitalRead(MISO)));
    
    // Send Rising edge
    digitalWrite(SCLK, HIGH);
    
    // Hold Time
   delay(1/1000);
    
    // Send Falling edge
    digitalWrite(SCLK, LOW);
  }
  return rx_byte;
}
 byte get_temp_temp()
{
  // Retrieve the manufacture ID number 
  // 8 bit read only register where bit 3-7 is the Manufacture ID
   // Send command byte to read from address 0x03 -> Command byte goes to 0x01 destination
  send_data(0x40, CONFIGURATION_ADDR);  
  // Read 8 bits
   byte rx_data = 0x00;
  rx_data = read_byte();
   Serial.println("STATUS REG: " + String(rx_data));
}
 byte read_ID()
{
  // Retrieve the manufacture ID number 
  // 8 bit read only register where bit 3-7 is the Manufacture ID
   // Send command byte to read from address 0x03 -> Command byte goes to 0x01 destination
  send_data(0x58, CONFIGURATION_ADDR);  
  // Read 8 bits
   byte rx_data = 0x00;
  rx_data = read_byte();
   Serial.println(String(rx_data));
}
 void configure_temp_sensor()
{
  // Write 0x80 to register 0x01
  send_data(CONFIGURATION_DATA, CONFIGURATION_ADDR);
}
 int get_temp_readings()
{
  int temp = 0x0000;
  // Send 16 clock pulses to retreive temp reading
  for(int i = 15; i > -1; i--)
  {
    // Set up time
   delay(1/1000);
    // Read bit from DOUT
    temp |= (digitalRead(MISO) << i);
    
    // Send rising edge
    digitalWrite(SCLK, HIGH);
     // Hold time
   delay(1/1000);
    // Send falling edge
   digitalWrite(SCLK, LOW);
  }
  return temp;
}
 void check_temp()
{
  int temp = get_temp_readings();
  if((temp == 0x0000) or (temp == 0xFFFF))
  {
    Serial.println(String(temp));
    end_TX();
   delay(1/1000);
    start_TX();
    enable_continuous_read_mode();
  }
  else
  {
    Serial.println(String(temp / 128));
  }
}
