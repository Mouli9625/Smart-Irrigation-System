#include <SoftwareSerial.h>
#include <LiquidCrystal.h>
#include <DFRobot_DHT11.h>
DFRobot_DHT11 DHT;
#define DHT11_PIN A3
SoftwareSerial mySerial(6,7);

const int rs = 8, en = 9, d4 = 10, d5 = 11, d6 = 12, d7 = 13;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int kk=0;
int moi=A4;
int rss=A5;
int mval,rval,hval,tval;
int cnt=0;
int pmp=2;
int pmp1=3;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
mySerial.begin(9600);
delay(200);
lcd.begin(16, 2);
lcd.print("   WELCOME");
pinMode(pmp,OUTPUT);
pinMode(pmp1,OUTPUT);
digitalWrite(pmp1,0);
digitalWrite(pmp,0);
delay(200);

}

void loop() {
  // put your main code here, to run repeatedly:


mval=100-analogRead(moi)/10.23;
rval=100-analogRead(rss)/10.23;
DHT.read(DHT11_PIN);
tval=DHT.temperature;
hval=DHT.humidity;



lcd.clear();
lcd.print("T:"+String(tval) + " H:"+String(hval) );
lcd.setCursor(0,1);
lcd.print("M:"+ String(mval)+ " R:"+String(rval) );
if(digitalRead(pmp1)==1)
{
   lcd.setCursor(13,1);
    lcd.print("ON ");
}
else
{
 lcd.setCursor(13,1);
    lcd.print("OFF");  
}



if(Serial.available())
{
  int x=Serial.read();
  if(x=='1')
  {
    lcd.setCursor(13,1);
    lcd.print("ON ");
    digitalWrite(pmp1,1);
digitalWrite(pmp,0);
    
  }

   if(x=='2')
  {
    lcd.setCursor(13,1);
    lcd.print("OFF");
    digitalWrite(pmp1,0);
digitalWrite(pmp,0);
    
  }
}

if(mySerial.available())
{
  int y=mySerial.read();
   if(y=='1')
  {
    lcd.setCursor(13,1);
    lcd.print("ON ");
    digitalWrite(pmp1,1);
digitalWrite(pmp,0);
    
  }

   if(y=='2')
  {
    lcd.setCursor(13,1);
    lcd.print("OFF");
    digitalWrite(pmp1,0);
digitalWrite(pmp,0);
    
  }
}

delay(1000);
cnt=cnt+1;
if(cnt>15)
{
  cnt=0;
  Serial.println(String(tval) +","+String(hval)+","+String(rval)+","+String(mval));
  mySerial.println("285266,XTQD8VAFQLS00GOQ,303007,B5RINZ9KQOHFA70Z,SRC 24G,src@internet,"+String(tval) +","+String(hval)+","+String(rval)+","+String(mval) +","+String(digitalRead(pmp1))+",\n");

}
}
