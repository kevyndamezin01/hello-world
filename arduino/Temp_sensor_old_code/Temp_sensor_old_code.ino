// This is to communicate with the ADT7310 Temperature Sensor using the Arduino Uno. 
// This will allow a user to gain a stream of temperature readings from 
// the sensor using a list of pre programmed commands.  
boolean rxComplete = false;
String inputString = "";
int debug = 0;
#define CONFIGURATION_DATA 0x80
#define CONFIGURATION_ADDR 0x01
// This is the configuration address
#define ENABLE_1SPS_MODE_DATA 0x40
// Write 0x40 to register 0x01 to enable 1 SPS mode
#define ENABLE_CONTINUOUS_READ_DATA 0x54
// Write 0x54 to register 0x01 to enable continous read mode
#define DISABLE_CONTINUOUS_READ_DATA 0X50
// Write 0x54 to register 0x01 to disable continous read mode
#define ENABLE_SHUTDOWN_DATA 0x60
// Write 0x60 to 0x01 to enable shutdown
#define DISABLE_SHUTDOWN_DATA 0xC0
// Write 0xC0 to disable shutdown mode
#define ID_REGISTER_ADDR 0x03
// This is the ID Register address
#define SCLK 7
#define MISO 11
#define MOSI 12
#define CS 5
void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
Serial.println("Temperautre Sensor!");
welcome_message();
pinMode(SCLK, OUTPUT);
pinMode(MISO, INPUT);
pinMode(CS, OUTPUT);
pinMode(MOSI, OUTPUT);
digitalWrite(CS, HIGH);
digitalWrite(SCLK, HIGH);
digitalWrite(MOSI, HIGH);
start_TX();
configure_temp_sensor();
end_TX();
start_TX();
enable_1SPS_mode();
end_TX();
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
      Serial.println("To begin a stream of data use 'help off'");
      Serial.println("To begin a stream of temperature readings use 'get temp'");
      Serial.println("To cancle the stream of temperature readings use 'turn temp off'");
      Serial.println("To retrieve the manufacture number use 'get manufacture number'");
      debug = 0;
    }
    else if (inputString == "help off")
    {
      Serial.println("Finished with help message, turning debug back on!");
      debug = 1;
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
    if(inputString == "get temp")
    {
      Serial.println("Starting temperature readings");
      reset_temp_sensor();
      start_TX();
      enable_continuous_read_mode();
    }
    if(inputString == "turn temp off")
    {
      Serial.println("Turning temperature readings off");
      end_TX();
      disable_continuous_read_mode();
    }
    if(inputString == "get manufacturer number")
    {
      Serial.println("Retreiving manufacture number");
      reset_temp_sensor();
      start_TX();
      read_ID();
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
void write_byte(byte data)
{
  // Send MSB first
  
  // For each BIT in DATA: 
  for( int i = 7; i > -1; i--)
  {
    // Put BIT on MOSI
    digitalWrite(MOSI, bitRead(data, i));
    // Setup delay
    delay(1);
    // Take SCLK high
    digitalWrite(SCLK, HIGH);
    
    // Hold delay 
    delay(1);
    
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
  
    // ADT7130 will reset if 32 consecutive 1's are transmitted
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
    delay(1);
    
    // Read bit from DOUT
    rx_byte |= (digitalRead(MISO) << i);
    // Serial.println("Read bit: " + String(digitalRead(MISO)));
    
    // Send Rising edge
    digitalWrite(SCLK, HIGH);
    
    // Hold Time
    delay(1);
    
    // Send Falling edge
    digitalWrite(SCLK, LOW);
  }
  return rx_byte;
}
byte read_ID()
{
  // Retrieve the manufacture ID number 
  // 8 bit read only register where bit 3-7 is the Manufacture ID
  digitalWrite(CS, LOW);
  // Send command byte to read from address 0x03 -> Command byte goes to 0x01 destination
  send_data(0x58, CONFIGURATION_ADDR);  
  // Read 8 bits
  byte rx_data = 0x00;
  rx_data = read_byte();
  Serial.println("Read manufacture ID: " + String(rx_data));
  digitalWrite(CS, HIGH);
}
void configure_temp_sensor()
{
   // Write 0x80 to register 0x01
  send_data(CONFIGURATION_DATA, CONFIGURATION_ADDR);
}
int get_temp_readings()
{
  digitalWrite(MISO, HIGH);
  digitalWrite(MOSI, LOW);
  
  int temp = 0x0000;
  // Send 16 clock pulses to retreive temp reading
  for(int i = 15; i > -1; i--)
  {
    // Set up time
    delay(1);
    // Read bit from DOUT
    temp |= (digitalRead(MISO) << i);
    Serial.println("Read bit: " + String(digitalRead(MISO)));
  
    
    // Send rising edge
    digitalWrite(SCLK, HIGH);
    // Hold time
    delay(1);
   // Send falling edge
   digitalWrite(SCLK, LOW);
  }
  Serial.println("Read Temp in degrees: " + String(temp / 128));
  return temp;
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
}
void disable_continuous_read_mode()
{
  // Write 0x50 to register 0x01
  send_data(DISABLE_CONTINUOUS_READ_DATA, CONFIGURATION_ADDR);
}
// ---------------------------------------------
void welcome_message()
{
  if (debug == 1)
  {
    Serial.println("Temperature Sensor... lets get some data!!");
  }
}
void loop()
{  // put your main code here, to run repeatedly:
  delay(1000);
  process_uart_messages();
  get_temp_readings();
}
