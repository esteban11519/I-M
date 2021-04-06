//String cad;
int led = 13;
int potPin = A2;
int val = 0;
int auxVal=0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(potPin, INPUT);
}



void loop() {
  // put your main code here, to run repeatedly:
  val=analogRead(potPin);
  //if(val!=auxVal)
  //{
    Serial.println(val);
  //  auxVal=val;
  //}
  delay(500);
  /*
    digitalWrite(led,1);
    delay(500);
    digitalWrite(led,0);
    delay(500);
  */
  /*
    if (Serial.available())
    {
     cad = Serial.readString();
     on=cad.toInt();
     digitalWrite(led,on);
    }
    delay(100);
  */
}
