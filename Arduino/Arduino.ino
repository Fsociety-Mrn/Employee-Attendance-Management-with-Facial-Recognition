#include <SPI.h>
#include <MFRC522.h>
#include <LiquidCrystal_I2C.h>


/*
* Typical pin layout used:
* -----------------------------------------------------------------------------------------
*             MFRC522      Arduino       Arduino   Arduino    Arduino          Arduino
*             Reader/PCD   Uno/101       Mega      Nano v3    Leonardo/Micro   Pro Micro
* Signal      Pin          Pin           Pin       Pin        Pin              Pin
* -----------------------------------------------------------------------------------------
* RST/Reset   RST          9             5         D9         RESET/ICSP-5     RST
* SPI SS      SDA(SS)      10            53        D10        10               10
* SPI MOSI    MOSI         11 / ICSP-4   51        D11        ICSP-4           16
* SPI MISO    MISO         12 / ICSP-1   50        D12        ICSP-1           14
* SPI SCK     SCK          13 / ICSP-3   52        D13        ICSP-3           15
*
* More pin layouts for other boards can be found here: https://github.com/miguelbalboa/rfid#pin-layout
*/

#define SS_PIN 10
#define RST_PIN 9


#define GREEN_LED 3 //GREEN LED
#define  RED_LED 4 //RED LED
#define  LOCKED  5 //FOR LOCKED


// Instance of the class MFRC522
MFRC522 rfid(SS_PIN, RST_PIN);

//i2c lcd
LiquidCrystal_I2C lcd(0x27,20,4); 

void setup() {
  
  Serial.begin(9600);

  SPI.begin(); // Init SPI bus
  rfid.PCD_Init(); // Init MFRC522

  lcd.init(); 
  lcd.backlight(); 

  pinMode(GREEN_LED,OUTPUT); 
  pinMode(RED_LED,OUTPUT);
  pinMode(LOCKED,OUTPUT);

  lcd.clear();
  lcd.print("RFID Entry");
  digitalWrite(GREEN_LED,LOW);
  digitalWrite(RED_LED,HIGH);  
}

String b;
int Number;

void loop() {
  // put your main code here, to run repeatedly:
     RFID();

  while (Serial.available()>0) {
 
    int incomingByte = 0;
    b = Serial.readStringUntil('\n');
    Number = b.toInt();

    if (Number == 1){

      tone(6,440,800);
      lcd.clear();
      lcd.print("access granted");
      digitalWrite(LOCKED,HIGH);
      digitalWrite(GREEN_LED,HIGH);
      digitalWrite(RED_LED,LOW);
      
      
      delay(2000);
      lcd.clear();
      lcd.print("RFID Entry");

//      reset 
      digitalWrite(LOCKED,LOW);
      digitalWrite(GREEN_LED,LOW);
      digitalWrite(RED_LED,HIGH);
      break;
    }else{
      
      tone(6,300,1000);
      lcd.clear();
      lcd.print("access denied");
      
      digitalWrite(LOCKED,LOW);
      digitalWrite(GREEN_LED,LOW);
      digitalWrite(RED_LED,HIGH);
      break;
    }
    
  }

}


void RFID() {

  // Reset the loop if no new card present on the sensor/reader
  if ( ! rfid.PICC_IsNewCardPresent())
    return;

  // Verify if the NUID has been readed
  if ( ! rfid.PICC_ReadCardSerial())
    return;

  String RFID_SERIALNUMBER = "";

  
  for (byte i = 0; i < 4; i++) {

    RFID_SERIALNUMBER += String(rfid.uid.uidByte[i]);
  }
//9716117039

  if(RFID_SERIALNUMBER=="115137192151" || RFID_SERIALNUMBER=="9716117039"){
    digitalWrite(LOCKED,HIGH);
    digitalWrite(GREEN_LED,HIGH);
    digitalWrite(RED_LED,LOW);
    tone(6,440,500);
    lcd.clear();
    lcd.print("access granted");
    delay(2000);
    digitalWrite(LOCKED,LOW);
    digitalWrite(GREEN_LED,LOW);
    digitalWrite(RED_LED,HIGH);

    lcd.clear();
    lcd.print("RFIF ENRTY");
    return;
  }else{
    tone(6,400,200);
    Serial.flush();
    Serial.println(RFID_SERIALNUMBER);
  }

//  digitalWrite(GREEN_LED,1);
//  digitalWrite(RED_LED,0);
  delay(1000);
//  digitalWrite(GREEN_LED,0);
//  digitalWrite(RED_LED,1);

}
