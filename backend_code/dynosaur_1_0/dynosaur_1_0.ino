#define INT_0 2
#define INT_1 3
#define BUZZ 7
#define BUTT 8
#define LED_R 9
#define LED_G 6
#define LED_B 10
#define AF_0 A0
#define AF_1 A1

#define PPR 600

#define ENCODER

#define TEST_TIME 5000000 //In microseconds, the total test runtime

#define SAMPLE_TIME 20000 //In microseconds, time per "division"

#define MAX_SPEED 800 //In pulses, NEED TO TUNE

volatile unsigned long pulses = 0;

unsigned long prevTime;
unsigned long currentTime;

bool tooFast;

void setup() {
  // put your setup code here, to run once:
  pinMode(INT_0, INPUT_PULLUP);
  pinMode(INT_1, INPUT_PULLUP);
  pinMode(BUZZ, OUTPUT); digitalWrite(BUZZ, LOW);
  pinMode(LED_R, OUTPUT); digitalWrite(LED_R, LOW);
  pinMode(LED_G, OUTPUT); digitalWrite(LED_G, LOW);
  pinMode(LED_B, OUTPUT); digitalWrite(LED_B, LOW);
  attachInterrupt(digitalPinToInterrupt(INT_0), encoder, CHANGE);
  attachInterrupt(digitalPinToInterrupt(INT_1), encoder, CHANGE);
  Serial.begin(1152000);
}

void loop() {
  currentTime = micros();
  if(pulses == 0) {
    digitalWrite(LED_R, LOW);
    digitalWrite(LED_G, HIGH);
    digitalWrite(LED_B, LOW);
  } else if (pulses < MAX_SPEED) {
    digitalWrite(LED_R, HIGH);
    digitalWrite(LED_G, HIGH);
    digitalWrite(LED_B, LOW);
    digitalWrite(BUZZ, LOW);
  } else {
    digitalWrite(LED_R, HIGH);
    digitalWrite(LED_G, LOW);
    digitalWrite(LED_B, LOW);
    digitalWrite(BUZZ, HIGH);
  }
  if (currentTime - prevTime >= SAMPLE_TIME) {
    Serial.println((pulses/PPR) * 360);
    pulses = 0;
  }
}

void encoder() {
  pulses++;
}

