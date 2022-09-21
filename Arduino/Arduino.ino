
int GREEN_LED = 3;
int RED_LED = 4;

void setup() {

  Serial.begin(9600);
  pinMode(GREEN_LED,OUTPUT); 
  pinMode(RED_LED,OUTPUT);

  digitalWrite(GREEN_LED,LOW);
  digitalWrite(RED_LED,HIGH);  
}

String b;
int Number;

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    int incomingByte = 0;
    b = Serial.readStringUntil('\n');
    Number = b.toInt();

    if (Number == 1){
      digitalWrite(GREEN_LED,Number);
      digitalWrite(RED_LED,LOW);
      delay(2000);
    }else{
      digitalWrite(GREEN_LED,LOW);
      digitalWrite(RED_LED,HIGH);
    }

    
  }

}
