int buttonPin = 3;  
int ledPin = 13; 
int ledPin1 = 12;
int ledPin2 = 11;
int ledPin3 = 10;
int ledPin4 = 9;

int buttonState = 0; //variável -> está inclinando se é 5 ou 0

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) { //1 = 5V = HIGH - Ligado
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW); //0 = 0V = LOW - Desligado
  }
  
  if (buttonState == HIGH) { 
    digitalWrite(ledPin1, LOW);
  } else {
    digitalWrite(ledPin1, LOW); 
  }
  
  if (buttonState == LOW) { 
    digitalWrite(ledPin2, HIGH);
  } else {
    digitalWrite(ledPin2, LOW); 
  }
  
  if (buttonState == HIGH) { 
    digitalWrite(ledPin3, LOW);
  } else {
    digitalWrite(ledPin3, HIGH); 
  }
  
  if (buttonState == HIGH) { 
    digitalWrite(ledPin4, HIGH);
  } else {
    digitalWrite(ledPin4, LOW); 
  }
}
