#define INT_0 2
#define INT_1 3
#define BUZZ 7
#define LED_R 9
#define LED_G 6
#define LED_B 10
#define AF_0 A0
#define AF_1 A1

#define PPR 600

#define ENCODER

#define TEST_TIME 5000000 //In microseconds, the total test runtime

#define SAMPLE_FREQ 0.05 //In microseconds, time per "division"

#define MAX_SPEED 4 //In pulses, NEED TO TUNE

const long SAMPLE_TIME = 500000;

volatile long pulses = 0;
long prevPulses = 0;

double velocity = 0;
double prevVelocity = 0;

double acceleration = 0;

unsigned long prevTime = 0;
unsigned long currentTime = 0;

bool tooFast;

void setup() {
  // put your setup code here, to run once:
  pinMode(INT_0, INPUT_PULLUP);
  pinMode(INT_1, INPUT_PULLUP);
  pinMode(BUZZ, OUTPUT); digitalWrite(BUZZ, LOW);
  pinMode(LED_R, OUTPUT); digitalWrite(LED_R, LOW);
  pinMode(LED_G, OUTPUT); digitalWrite(LED_G, LOW);
  pinMode(LED_B, OUTPUT); digitalWrite(LED_B, LOW);
  attachInterrupt(digitalPinToInterrupt(2), encoder, CHANGE);
  attachInterrupt(digitalPinToInterrupt(3), encoder, CHANGE);
  Serial.begin(115200);
}

void loop() {
  currentTime = micros();
  if(pulses == 0) {
    digitalWrite(LED_R, HIGH);
    digitalWrite(LED_G, LOW);
    digitalWrite(LED_B, HIGH);
    digitalWrite(BUZZ, LOW);
  } else if (pulses < MAX_SPEED) {
    digitalWrite(LED_R, LOW);
    digitalWrite(LED_G, LOW);
    digitalWrite(LED_B, HIGH);
    digitalWrite(BUZZ, LOW);
  } else {
    digitalWrite(LED_R, LOW);
    digitalWrite(LED_G, HIGH);
    digitalWrite(LED_B, HIGH);
    digitalWrite(BUZZ, HIGH);
  }
  if (currentTime - prevTime >= SAMPLE_TIME) {
    updateVars();
    Serial.print(velocity, 4); Serial.print(", "); Serial.println(acceleration, 4);
    pulses = 0;
    prevTime = currentTime;
  }
  //Serial.print(pulses); Serial.print(", "); Serial.println(prevPulses);
}

void encoder() {
  pulses++;
}

void updateVars() {
  velocity = pulsesToDegrees(pulses) / (SAMPLE_TIME / 10000);
  acceleration = (velocity - prevVelocity) / (SAMPLE_TIME / 10000);
  prevPulses = pulses;
  prevVelocity = velocity;
}

double pulsesToDegrees(int i) {
  return (double(i) / PPR) * 360;
}

