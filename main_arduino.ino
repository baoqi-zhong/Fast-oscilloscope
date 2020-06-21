// 波特率38400
// 采样端口：A0
void setup() {
  Serial.begin(38400);
  pinMode(A0,INPUT);
}

void loop() {
  Serial.println(analogRead(A0));
}
