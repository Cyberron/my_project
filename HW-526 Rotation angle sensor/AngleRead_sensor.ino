int sensorPin = A0;    // select the input pin for the potentiometer
int sensorValue = 0;  // variable to store the value coming from the sensor
float ans;
float maxa = 682.0 ; // maxa is the highest analog value(approximately) that can read from sensor

void setup() {
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(sensorPin);
  Serial.print("analog raw = ");
  Serial.println(sensorValue);
  Serial.print("        cw_angle = ");
  Serial.println( cwangle(sensorValue) );
  Serial.print("            ccw_angle = ");
  Serial.println( ccwangle(sensorValue) );
  Serial.print("                    angle = ");
  Serial.println( cwangle(sensorValue) + ccwangle(sensorValue) );
  delay(200);
}

float cwangle(int x){
  ans = ((360.0 * x)/maxa);
  return ans;
  }


float ccwangle(int x){
  ans = ((360.0 * abs(maxa-x))/maxa);
  return ans;
  }
